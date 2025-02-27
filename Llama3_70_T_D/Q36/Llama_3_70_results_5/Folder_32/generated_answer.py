def filter_chars(s):
    chars_to_remove = [c for c in s[40:63] if '7' < c < 'H']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s