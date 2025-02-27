def filter_chars(s):
    chars_to_remove = [c for c in s[70:74] if 'A' < c < 'U']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s