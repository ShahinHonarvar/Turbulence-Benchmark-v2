def filter_chars(s):
    if len(s) <= 55:
        return s
    chars_to_remove = set((c for c in s[56:84] if ';' < c < 'z'))
    return ''.join((c for c in s if c not in chars_to_remove))