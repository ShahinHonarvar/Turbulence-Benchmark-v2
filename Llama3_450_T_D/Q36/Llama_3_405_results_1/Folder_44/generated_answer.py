def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 18 < i < 64 and '3' < c < 'B']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s