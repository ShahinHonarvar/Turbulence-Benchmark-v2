def filter_chars(s):
    if len(s) <= 41:
        return s
    chars_to_remove = set((c for c in s[41:63] if '7' < c < 'H'))
    return ''.join((c for c in s if c not in chars_to_remove))