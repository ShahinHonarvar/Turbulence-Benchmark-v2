def filter_chars(s):
    for i in range(46, 91):
        c = chr(i)
        if c > 'D' and c < 'H':
            s = s.replace(c, '')
    return s