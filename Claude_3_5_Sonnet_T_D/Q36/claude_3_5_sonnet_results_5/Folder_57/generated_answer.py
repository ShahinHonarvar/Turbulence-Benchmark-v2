def filter_chars(s):
    to_remove = set((c for c in s[71:74] if 'A' < c < 'U'))
    return ''.join((c for c in s if c not in to_remove))