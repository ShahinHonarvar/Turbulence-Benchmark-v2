def filter_chars(s):
    chars_to_remove = set((c for c in s[24:83] if 'f' < c < 'o'))
    return ''.join((c for c in s if c not in chars_to_remove))