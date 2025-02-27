def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 37 <= i <= 56 and '6' <= c <= '_'))
    return ''.join((c for c in s if c not in to_remove))