def filter_chars(s):
    target_chars = set((c for i, c in enumerate(s) if 83 <= i <= 99 and '*' <= c <= 'j'))
    return ''.join((c for c in s if c not in target_chars))