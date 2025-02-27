def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 58 < i < 82 and 'F' < c < 'O']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s