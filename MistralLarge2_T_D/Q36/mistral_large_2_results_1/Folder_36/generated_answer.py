def filter_chars(s):
    to_remove = set((c for c in s[283:484] if 'l' < c < 't'))
    return ''.join((c for c in s if c not in to_remove))