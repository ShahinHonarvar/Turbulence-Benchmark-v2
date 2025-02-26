def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 17 <= i <= 63 and 'O' <= c <= '^'))
    return ''.join((c for c in s if c not in to_remove))