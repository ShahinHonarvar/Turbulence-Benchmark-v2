def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 69 <= i < 87 and '#' < c < 'L'))
    return ''.join((c for c in s if c not in chars_to_remove))