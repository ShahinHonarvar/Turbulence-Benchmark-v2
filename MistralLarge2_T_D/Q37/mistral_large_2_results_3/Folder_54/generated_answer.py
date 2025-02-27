def filter_chars(s):
    to_remove = set((c for c in s[46:86] if '-' <= c <= 'X'))
    return ''.join((c for c in s if c not in to_remove))