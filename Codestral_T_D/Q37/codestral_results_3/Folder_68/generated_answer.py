def filter_chars(s):
    for c in s[7:10]:
        if '6' <= c <= 'w':
            s = s.replace(c, '')
    return s