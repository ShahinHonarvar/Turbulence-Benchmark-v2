def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 50 < i < 92 and 'A' < c < 'Q']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s