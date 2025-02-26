def filter_chars(s):
    to_remove = set((c for c in s[15:85] if 'I' < c < 'M'))
    return ''.join((c for c in s if c not in to_remove))