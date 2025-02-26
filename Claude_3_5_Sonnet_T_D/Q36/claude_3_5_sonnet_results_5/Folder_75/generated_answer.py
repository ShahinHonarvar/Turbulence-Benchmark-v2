def filter_chars(s):
    to_remove = set((c for c in s[47:74] if '&' < c < 'M'))
    return ''.join((c for c in s if c not in to_remove))