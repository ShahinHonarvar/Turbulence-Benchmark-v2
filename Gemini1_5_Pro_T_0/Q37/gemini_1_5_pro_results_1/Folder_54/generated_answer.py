def filter_chars(s):
    for i in range(46, 86):
        if i >= ord('-') and i <= ord('X'):
            c = chr(i)
            s = s.replace(c, '')
    return s