def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 61 < i < 88 and '%' < c < 'q']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s