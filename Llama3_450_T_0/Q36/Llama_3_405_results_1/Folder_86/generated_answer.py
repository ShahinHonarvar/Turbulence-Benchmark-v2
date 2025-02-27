def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 672 < i < 709 and 'X' < c < '}'))
    return ''.join((c for c in s if c not in chars_to_remove))