def filter_chars(s):
    chars_to_remove = [c for c in s[54:92] if 'J' < c < 'X']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s