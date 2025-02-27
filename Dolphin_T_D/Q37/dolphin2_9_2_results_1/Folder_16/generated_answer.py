def filter_chars(s):
    chars_to_filter = [c for c in s if c >= 'D' and c <= 'Y']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s