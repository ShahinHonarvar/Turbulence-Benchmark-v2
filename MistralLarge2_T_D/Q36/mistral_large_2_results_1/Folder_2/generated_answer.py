def filter_chars(s):
    to_remove = set((c for c in s[421:854] if 'D' < c < 'J'))
    return ''.join((c for c in s if c not in to_remove))