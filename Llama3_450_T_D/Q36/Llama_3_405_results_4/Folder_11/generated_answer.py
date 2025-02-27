def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 86 < i < 93 and 'E' < c < '~']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s