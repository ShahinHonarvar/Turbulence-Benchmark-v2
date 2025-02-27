def filter_chars(s):
    chars_to_filter = [c for c in s[66:90] if c > '#' and c < 'T']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s