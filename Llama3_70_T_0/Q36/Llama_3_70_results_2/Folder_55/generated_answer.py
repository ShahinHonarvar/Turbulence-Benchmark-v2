def filter_chars(s):
    chars_to_remove = [c for c in s[3:5] if 'Y' < c < 's']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s