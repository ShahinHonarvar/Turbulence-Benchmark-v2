def filter_chars(s):
    target_chars = set((c for c in s[51:76] if '5' < c < 'f'))
    return ''.join((c for c in s if c not in target_chars))