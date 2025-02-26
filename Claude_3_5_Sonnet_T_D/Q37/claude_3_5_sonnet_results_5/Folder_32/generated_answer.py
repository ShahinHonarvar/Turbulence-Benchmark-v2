def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 23 <= i <= 89 and 'w' <= c <= '{'))
    return ''.join((c for c in s if c not in to_remove))