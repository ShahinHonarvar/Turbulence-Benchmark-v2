def filter_chars(s):
    to_remove = set((c for c in s[171:636] if 'c' < c < 's'))
    return ''.join((c for c in s if c not in to_remove))