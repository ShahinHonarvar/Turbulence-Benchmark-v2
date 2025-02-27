def filter_chars(s):
    to_remove = set((c for c in s[12:26] if 'P' <= c <= 'x'))
    return ''.join((c for c in s if c not in to_remove))