def filter_chars(s):
    chars_to_remove = [c for c in s[56:68] if '9' < c < 'W']
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s