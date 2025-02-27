def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 58 <= i < 81 and '5' < c < '>'))
    return ''.join((c for c in s if c not in chars_to_remove))