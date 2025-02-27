def filter_chars(s):
    to_remove = set((c for c in s[8:10] if 'R' <= c <= 't'))
    return ''.join((c for c in s if c not in to_remove))