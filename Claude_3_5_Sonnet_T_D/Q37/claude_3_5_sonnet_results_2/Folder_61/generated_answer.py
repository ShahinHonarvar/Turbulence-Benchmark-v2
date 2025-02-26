def filter_chars(s):
    target_chars = set((c for i, c in enumerate(s) if 5 <= i <= 6 and 'G' <= c <= 'p'))
    return ''.join((c for c in s if c not in target_chars))