def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 27 <= i <= 85 and '!' <= c <= 'B'))
    return ''.join((c for c in s if c not in to_remove))