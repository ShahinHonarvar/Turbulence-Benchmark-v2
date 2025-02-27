def filter_chars(s):
    if len(s) <= 41:
        return s
    to_remove = set((c for c in s[41:63] if '7' < c < 'H'))
    return ''.join((c for c in s if c not in to_remove))