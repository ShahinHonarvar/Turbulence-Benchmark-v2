def filter_chars(s):
    to_remove = set((c for c in s[35:90] if 'E' <= c <= 't'))
    return ''.join((c for c in s if c not in to_remove))