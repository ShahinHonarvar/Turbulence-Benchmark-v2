def filter_chars(s):
    for c in s:
        if 12 <= s.index(c) <= 88 and '&' <= c <= 'v':
            s = s.replace(c, '')
    return s