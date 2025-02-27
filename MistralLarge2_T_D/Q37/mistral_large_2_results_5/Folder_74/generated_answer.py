def filter_chars(s):
    to_remove = set((c for c in s[19:33] if 'f' <= c <= 'o'))
    return ''.join((c for c in s if c not in to_remove))