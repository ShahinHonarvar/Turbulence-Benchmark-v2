def filter_chars(s):
    to_remove = set((c for c in s[35:60] if '!' < c < 'B'))
    return ''.join((c for c in s if c not in to_remove))