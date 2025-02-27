def filter_chars(s):
    chars_to_filter = [c for c in s[13:40] if ':' < c < 'C']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s