def filter_chars(s):
    chars_to_filter = [c for c in s[2:4] if '5' <= c >= '_']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s