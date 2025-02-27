def filter_chars(s):
    chars_to_filter = [c for c in s if 12 <= s.index(c) <= 88 and '&' <= c <= 'v']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s