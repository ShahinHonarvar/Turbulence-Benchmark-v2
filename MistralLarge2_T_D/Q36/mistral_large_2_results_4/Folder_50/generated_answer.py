def filter_chars(s):
    to_remove = set((c for c in s[61:88] if '%' < c < 'q'))
    return ''.join((c for c in s if c not in to_remove))