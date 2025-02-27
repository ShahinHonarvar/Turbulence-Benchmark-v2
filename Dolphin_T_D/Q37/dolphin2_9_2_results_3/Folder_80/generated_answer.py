def filter_chars(s):
    chars_to_filter = [c for c in s if 36 <= s.index(c) <= 79 and 'a' <= c <= 'i']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s