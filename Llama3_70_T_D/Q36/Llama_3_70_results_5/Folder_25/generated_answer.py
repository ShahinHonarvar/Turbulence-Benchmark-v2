def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 24 < i < 37 and 'A' < c < 'h']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s