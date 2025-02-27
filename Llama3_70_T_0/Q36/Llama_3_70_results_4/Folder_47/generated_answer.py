def filter_chars(s):
    chars_to_remove = [c for c in s[45:57] if 'F' < c < 'n']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s