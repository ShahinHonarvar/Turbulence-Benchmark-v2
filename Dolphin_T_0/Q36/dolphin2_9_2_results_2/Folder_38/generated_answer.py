def filter_chars(s):
    chars_range = s[44:48]
    for c in chars_range:
        if '+' < c < 'l':
            s = s.replace(c, '')
    return s