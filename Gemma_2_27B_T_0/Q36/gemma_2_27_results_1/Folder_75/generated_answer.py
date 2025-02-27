def filter_chars(s):
    for i in range(46, 74):
        c = chr(i)
        if c > '&' and c < 'M':
            s = s.replace(c, '')
    return s