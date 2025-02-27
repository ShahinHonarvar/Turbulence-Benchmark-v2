def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 477 <= i <= 984 and ',' <= c <= 'V'))
    return ''.join((c for c in s if c not in to_remove))