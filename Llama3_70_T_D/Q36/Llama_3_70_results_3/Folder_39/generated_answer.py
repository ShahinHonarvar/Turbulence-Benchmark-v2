def filter_chars(s):
    chars_to_remove = [c for c in s[43:59] if '5' < c < 'C']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s