def filter_chars(s):
    chars_to_remove = [c for c in s[46:74] if '&' < c < 'M']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s