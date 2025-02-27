def filter_chars(s):
    range_chars = set((c for c in s[71:97] if '_' <= c <= 'o'))
    return ''.join((c for c in s if c not in range_chars))