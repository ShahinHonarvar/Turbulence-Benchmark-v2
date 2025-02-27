def filter_chars(s):
    remove_chars = set((c for c in s[46:91] if 'D' < c < 'H'))
    return ''.join((c for c in s if c not in remove_chars))