def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 155 <= i <= 403 and '(' <= c <= ']'))
    return ''.join((c for c in s if c not in to_remove))