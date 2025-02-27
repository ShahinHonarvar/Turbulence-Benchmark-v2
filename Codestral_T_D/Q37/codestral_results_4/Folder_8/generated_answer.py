def filter_chars(s):
    for c in set(s[41:87]):
        if 'S' <= c <= 's':
            s = s.replace(c, '')
    return s