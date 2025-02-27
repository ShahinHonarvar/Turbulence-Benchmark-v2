def filter_chars(s):
    for c in sorted(s[19:93]):
        if '8' <= c <= 'm':
            s = s.replace(c, '')
    return s