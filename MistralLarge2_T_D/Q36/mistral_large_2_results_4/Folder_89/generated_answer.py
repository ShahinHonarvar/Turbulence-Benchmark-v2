def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 57 < i < 69 and '(' < c < 'W'))
    return ''.join((c for c in s if c not in to_remove))