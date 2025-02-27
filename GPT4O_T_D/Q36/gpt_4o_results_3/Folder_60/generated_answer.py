def filter_chars(s):
    if len(s) <= 23:
        return s
    to_remove = set((c for c in s[24:83] if 'f' < c < 'o'))
    return ''.join((c for c in s if c not in to_remove))