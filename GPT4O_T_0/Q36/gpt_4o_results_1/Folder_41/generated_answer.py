def filter_chars(s):
    if len(s) <= 81:
        return s
    chars_to_remove = set((c for c in s[82:89] if 'f' < c < '{'))
    return ''.join((c for c in s if c not in chars_to_remove))