def filter_chars(s):
    remove_chars = set((c for c in s[24:37] if 'A' < c < 'h'))
    return ''.join((c for c in s if c not in remove_chars))