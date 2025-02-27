def filter_chars(s):
    to_remove = set((c for c in s[10:53] if '@' <= c <= 'T'))
    return ''.join((c for c in s if c not in to_remove))