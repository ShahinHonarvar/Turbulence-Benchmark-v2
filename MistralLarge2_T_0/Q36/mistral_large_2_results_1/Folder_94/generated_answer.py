def filter_chars(s):
    chars_to_remove = set((c for c in s[15:85] if 'I' < c < 'M'))
    return ''.join((c for c in s if c not in chars_to_remove))