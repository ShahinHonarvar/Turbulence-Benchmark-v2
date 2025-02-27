def filter_chars(s):
    chars_to_filter = [c for c in s[24:83] if c >= '5' and c <= '<']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s