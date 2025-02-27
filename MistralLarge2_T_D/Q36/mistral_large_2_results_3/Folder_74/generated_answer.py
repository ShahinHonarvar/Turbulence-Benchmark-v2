def filter_chars(s):
    to_remove = set((c for c in s[33:36] if '>' < c < 'A'))
    return ''.join((c for c in s if c not in to_remove))