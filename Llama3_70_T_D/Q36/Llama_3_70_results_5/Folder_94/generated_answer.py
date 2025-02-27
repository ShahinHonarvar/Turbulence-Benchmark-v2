def filter_chars(s):
    chars_to_remove = [c for c in s[15:85] if 'I' < c < 'M']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s