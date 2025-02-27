def filter_chars(s):
    chars_to_remove = set(s[24:37])
    chars_to_remove = [c for c in chars_to_remove if 'A' < c < 'h']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s