def filter_chars(s):
    chars_to_remove = [c for c in s[61:88] if '%' < c < 'q']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s