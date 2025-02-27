def filter_chars(s):
    chars_to_remove = [c for c in s[43:69] if 'B' < c < 'r']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s