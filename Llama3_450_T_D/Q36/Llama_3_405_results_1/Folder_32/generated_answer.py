def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 40 < i < 63 and '7' < c < 'H'))
    return ''.join((c for c in s if c not in chars_to_remove))