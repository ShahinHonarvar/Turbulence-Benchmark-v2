def filter_chars(s):
    chars_to_remove = [c for c in s[58:82] if 'F' < c < 'O']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s