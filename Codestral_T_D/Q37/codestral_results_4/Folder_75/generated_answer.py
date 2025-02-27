def filter_chars(s):
    for c in s[34:68]:
        if 'W' <= c <= 'x':
            s = s.replace(c, '')
    return s