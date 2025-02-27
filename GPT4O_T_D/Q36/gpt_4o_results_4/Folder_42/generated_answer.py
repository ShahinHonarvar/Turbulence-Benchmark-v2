def filter_chars(s):
    chars_to_remove = set((c for c in s[43:68] if 't' < c < 'x'))
    return ''.join((c for c in s if c not in chars_to_remove))