def filter_chars(s):
    chars_to_filter = [c for c in s[22:86] if '7' <= c <= 'e']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s