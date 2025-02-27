def filter_chars(s):
    chars_to_remove = [c for c in s[31:70] if 'B' < c < 'v']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s