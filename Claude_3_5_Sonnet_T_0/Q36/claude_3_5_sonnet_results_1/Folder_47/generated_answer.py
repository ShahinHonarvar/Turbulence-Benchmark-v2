def filter_chars(s):
    chars_to_remove = set((c for c in s[45:57] if 'F' < c < 'n'))
    return ''.join((c for c in s if c not in chars_to_remove))