def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 283 <= i < 484 and 'l' < c < 't'))
    return ''.join((c for c in s if c not in chars_to_remove))