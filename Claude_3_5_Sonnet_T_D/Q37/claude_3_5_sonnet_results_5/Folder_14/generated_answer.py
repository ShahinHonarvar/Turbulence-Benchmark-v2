def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 35 <= i <= 98 and 'A' <= c <= 'b'))
    return ''.join((c for c in s if c not in to_remove))