def filter_chars(s):
    for i in range(27, 86):
        c = chr(i)
        if '!' <= c <= 'B':
            s = s.replace(c, '')
    return s