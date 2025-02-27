def filter_chars(s):
    for c in s[63:89]:
        if '*' < c < 'w':
            s = s.replace(c, '')
    return s