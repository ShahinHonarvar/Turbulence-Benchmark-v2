def filter_chars(s):
    chars_to_remove = set((c for c in s[55:84] if ';' < c < 'z'))
    return ''.join((c for c in s if c not in chars_to_remove))