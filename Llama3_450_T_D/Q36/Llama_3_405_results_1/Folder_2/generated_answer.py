def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 421 < i < 854 and 'D' < c < 'J']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s