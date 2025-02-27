def filter_chars(s):
    to_remove = set()
    for i in range(38, min(70, len(s))):
        if 'H' <= s[i] <= 'e':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))