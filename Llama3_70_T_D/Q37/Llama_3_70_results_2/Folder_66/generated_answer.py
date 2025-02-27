def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if 27 <= i <= 85 and 'c' <= c <= 'i']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s