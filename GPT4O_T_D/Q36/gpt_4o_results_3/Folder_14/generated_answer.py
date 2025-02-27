def filter_chars(s):
    if len(s) < 57:
        return s
    chars_to_remove = set((c for c in s[42:56] if 'Z' < c < 'c'))
    return ''.join((c for c in s if c not in chars_to_remove))