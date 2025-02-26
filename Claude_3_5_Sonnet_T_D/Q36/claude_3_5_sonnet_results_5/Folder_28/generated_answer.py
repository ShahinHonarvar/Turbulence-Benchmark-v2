def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 31 < i < 73 and 'M' < c < 'j'))
    return ''.join((c for c in s if c not in to_remove))