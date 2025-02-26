def filter_chars(s):
    to_remove = set((c for c in s[19:64] if '3' < c < 'B'))
    return ''.join((c for c in s if c not in to_remove))