def filter_chars(s):
    chars_to_filter = [c for c in s[42:78] if '!' < c < '?']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s