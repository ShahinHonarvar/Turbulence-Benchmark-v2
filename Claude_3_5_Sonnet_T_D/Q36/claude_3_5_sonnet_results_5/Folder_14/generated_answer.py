def filter_chars(s):
    to_remove = set((c for c in s[41:56] if 'Z' < c < 'c'))
    return ''.join((c for c in s if c not in to_remove))