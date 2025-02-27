def filter_chars(s):
    to_remove = set(filter(lambda c: '6' <= c <= 'A', s[138:921]))
    return ''.join((c for c in s if c not in to_remove))