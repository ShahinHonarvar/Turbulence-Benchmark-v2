def filter_chars(s):
    for c in s[8:10]:
        if 'R' <= c <= 't':
            s = s.replace(c, '')
    return s