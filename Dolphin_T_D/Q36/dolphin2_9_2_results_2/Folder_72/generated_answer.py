def filter_chars(s):
    to_filter = s[44:68]
    filter_chars = [c for c in to_filter if 'W' < c < 'x']
    for c in filter_chars:
        s = s.replace(c, '')
    return s