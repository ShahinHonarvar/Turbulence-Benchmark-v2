def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 11 < i < 46 and '!' < c < 'A']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s