def filter_chars(s):
    to_remove = set((c for c in s[71:95] if 'K' <= c <= 'a'))
    return ''.join((c for c in s if c not in to_remove))