def filter_chars(s):
    to_remove = set((c for c in s[344:874] if 'f' < c < '~'))
    return ''.join((c for c in s if c not in to_remove))