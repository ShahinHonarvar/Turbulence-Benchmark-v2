def filter_chars(s):
    chars_to_filter = [c for i, c in enumerate(s) if 318 < i < 337 and 'B' < c < 'z']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s