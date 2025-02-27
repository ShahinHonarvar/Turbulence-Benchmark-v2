def filter_chars(s):
    to_remove = set((c for c in s[3:5] if 'Y' < c < 's'))
    return ''.join((c for c in s if c not in to_remove))