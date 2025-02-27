def filter_chars(s):
    chars = [c for c in s if 'A' < c < 'h']
    for c in chars:
        s = s.replace(c, '')
    return s