def filter_chars(s):
    chars_to_filter = [c for c in s[51:76] if '5' < c < 'f']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s