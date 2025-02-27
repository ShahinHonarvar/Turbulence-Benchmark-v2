def filter_chars(s):
    to_remove = set((c for c in s[45:57] if 'F' < c < 'n'))
    return ''.join((c for c in s if c not in to_remove))