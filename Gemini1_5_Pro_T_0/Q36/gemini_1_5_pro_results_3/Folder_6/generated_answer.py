def filter_chars(s):
    for i in range(31, 70):
        c = chr(i)
        if 'B' < c < 'v':
            s = s.replace(c, '')
    return s