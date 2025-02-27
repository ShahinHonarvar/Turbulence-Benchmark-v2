def filter_chars(s):
    to_remove = set((c for c in s[34:68] if 'W' <= c <= 'x'))
    return ''.join((c for c in s if c not in to_remove))