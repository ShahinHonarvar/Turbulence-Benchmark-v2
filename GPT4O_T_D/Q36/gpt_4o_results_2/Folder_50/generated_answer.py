def filter_chars(s):
    remove_chars = set((c for c in s[62:88] if '%' < c < 'q'))
    return ''.join((c for c in s if c not in remove_chars))