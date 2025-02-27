def filter_chars(s):
    chars_to_remove = [c for c in s[42:68] if 't' < c < 'x']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s