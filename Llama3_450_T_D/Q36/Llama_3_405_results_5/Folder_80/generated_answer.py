def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 54 < i < 92 and 'J' < c < 'X']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s