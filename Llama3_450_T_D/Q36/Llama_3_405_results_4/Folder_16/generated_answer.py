def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 331 < i < 713 and 'M' < c < '_'))
    return ''.join((c for c in s if c not in chars_to_remove))