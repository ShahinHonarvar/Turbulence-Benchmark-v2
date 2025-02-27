def filter_chars(s):
    chars_to_remove = [c for c in s[41:56] if 'Z' < c < 'c']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s