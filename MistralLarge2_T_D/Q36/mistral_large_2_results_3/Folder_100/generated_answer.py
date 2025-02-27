def filter_chars(s):
    to_remove = set((c for c in s[43:69] if 'B' < c < 'r'))
    return ''.join((c for c in s if c not in to_remove))