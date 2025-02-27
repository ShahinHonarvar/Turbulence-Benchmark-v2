def filter_chars(s):
    chars_to_remove = [c for c in s[2:7] if 'h' < c < 'k']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s