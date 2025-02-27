def filter_chars(s):
    for i in range(88, 91):
        c = chr(i)
        if 'J' <= c <= 'Q':
            s = s.replace(c, '')
    return s