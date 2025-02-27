def filter_chars(s):
    chars_to_remove = [c for c in s[46:86] if '-' <= c <= 'X']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s