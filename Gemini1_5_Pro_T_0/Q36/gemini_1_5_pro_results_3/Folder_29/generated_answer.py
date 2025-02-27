def filter_chars(s):
    for i in range(46, 68):
        if i >= ord('H') and i <= ord('s'):
            c = chr(i)
            s = s.replace(c, '')
    return s