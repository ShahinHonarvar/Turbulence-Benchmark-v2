def filter_chars(s):
    for i in range(46, 86):
        c = chr(i)
        if '-' <= c <= 'X':
            s = s.replace(c, '')
    return s