def filter_chars(s):
    chars_to_remove = set((c for c in s[47:91] if 'D' < c < 'H'))
    return ''.join((c for c in s if c not in chars_to_remove))