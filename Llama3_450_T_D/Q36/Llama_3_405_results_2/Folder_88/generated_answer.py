def filter_chars(s):
    chars_to_filter = [c for c in s[78:81] if 'S' < c < '[']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s