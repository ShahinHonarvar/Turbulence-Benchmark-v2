def filter_chars(s):
    chars_to_filter = [c for c in s[14:75] if '9' < c < 'K']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s