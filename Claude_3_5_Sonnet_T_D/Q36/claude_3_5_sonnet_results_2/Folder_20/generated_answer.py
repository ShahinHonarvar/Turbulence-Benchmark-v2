def filter_chars(s):
    to_remove = set((c for c in s[14:40] if ':' < c < 'C'))
    return ''.join((c for c in s if c not in to_remove))