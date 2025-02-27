def filter_chars(s):
    for i in range(34, 68):
        c = chr(i)
        if 'W' <= c <= 'x':
            s = s.replace(c, '')
    return s