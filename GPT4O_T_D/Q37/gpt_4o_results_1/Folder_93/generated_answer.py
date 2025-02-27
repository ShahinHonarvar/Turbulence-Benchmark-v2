def filter_chars(s):
    to_remove = set()
    for i, c in enumerate(s):
        if 38 <= i <= 69 and 'H' <= c <= 'e':
            to_remove.add(c)
    return ''.join((c for c in s if c not in to_remove))