def filter_chars(s):
    to_remove = set((c for c in s[63:89] if '*' < c < 'w'))
    return ''.join((c for c in s if c not in to_remove))