def filter_chars(s):
    for c in s:
        if 34 <= s.index(c) <= 67 and 'W' <= c <= 'x':
            s = s.replace(c, '')
    return s