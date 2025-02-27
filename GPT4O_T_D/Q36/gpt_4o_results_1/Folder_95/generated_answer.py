def filter_chars(s):
    to_remove = set((c for c in s[57:86] if '+' < c < 'w'))
    return ''.join((c for c in s if c not in to_remove))