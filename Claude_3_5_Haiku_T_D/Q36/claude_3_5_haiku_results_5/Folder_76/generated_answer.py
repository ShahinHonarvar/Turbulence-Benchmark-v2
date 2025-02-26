def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 669 < i < 888 and 'B' < c < 'Y'))
    return ''.join((c for c in s if c not in chars_to_remove))