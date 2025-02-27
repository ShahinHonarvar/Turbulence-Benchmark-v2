def filter_chars(s):
    to_remove = set((c for c in s[51:78] if 'V' <= c <= 'Y'))
    return ''.join((c for c in s if c not in to_remove))