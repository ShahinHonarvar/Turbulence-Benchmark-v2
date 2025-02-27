def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 23 < i < 83 and 'f' < c < 'o']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s