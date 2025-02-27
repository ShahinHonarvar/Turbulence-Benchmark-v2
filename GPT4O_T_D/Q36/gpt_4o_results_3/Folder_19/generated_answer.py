def filter_chars(s):
    to_remove = set((c for c in s[78:87] if ';' < c < 'r'))
    return ''.join((c for c in s if c not in to_remove))