def filter_chars(s):
    for c in [ch for ch in s[36:41] if 'H' <= ch <= 'e']:
        s = s.replace(c, '')
    return s