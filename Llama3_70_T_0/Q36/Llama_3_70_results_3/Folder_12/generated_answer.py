def filter_chars(s):
    chars_to_remove = [c for c in s[32:84] if 'm' < c < 'w']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s