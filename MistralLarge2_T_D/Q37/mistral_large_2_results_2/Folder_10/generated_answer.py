def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 63 <= i <= 84 and 'E' <= c <= '~'))
    return ''.join((c for c in s if c not in to_remove))