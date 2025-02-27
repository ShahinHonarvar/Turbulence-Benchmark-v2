def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 56 < i < 86 and '+' < c < 'w']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s