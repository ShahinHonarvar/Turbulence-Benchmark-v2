def filter_chars(s):
    to_remove = set()
    for c in s[69:87]:
        if '#' < c < 'L':
            to_remove.add(c)
    return ''.join((c for c in s if c not in to_remove))