def filter_chars(s):
    remove_chars = set((c for c in s[59:82] if 'F' < c < 'O'))
    return ''.join((c for c in s if c not in remove_chars))