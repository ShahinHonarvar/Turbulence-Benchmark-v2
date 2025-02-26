def filter_chars(s):
    to_remove = set((c for c in s[48:75] if '6' < c < '_'))
    return ''.join((c for c in s if c not in to_remove))