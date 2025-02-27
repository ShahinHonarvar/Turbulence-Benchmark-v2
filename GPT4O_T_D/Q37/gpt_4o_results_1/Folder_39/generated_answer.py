def filter_chars(s):
    removal_indices = range(52, 82)
    removal_chars = set((c for i, c in enumerate(s) if i in removal_indices and 'A' <= c <= 'U'))
    return ''.join((c for c in s if c not in removal_chars))