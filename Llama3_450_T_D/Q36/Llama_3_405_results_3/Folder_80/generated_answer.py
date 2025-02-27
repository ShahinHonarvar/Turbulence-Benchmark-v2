def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 54 < i < 92 and 'J' < c < 'X']
    return ''.join((c for c in s if c not in chars_to_remove))