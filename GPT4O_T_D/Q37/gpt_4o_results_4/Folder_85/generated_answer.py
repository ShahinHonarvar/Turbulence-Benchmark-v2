def filter_chars(s):
    to_remove = set((c for i, c in enumerate(s[28:66]) if 'O' <= c <= 'd'))
    return ''.join((c for c in s if c not in to_remove))