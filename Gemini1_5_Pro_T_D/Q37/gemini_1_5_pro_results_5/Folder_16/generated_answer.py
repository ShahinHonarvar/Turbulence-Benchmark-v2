def filter_chars(s):
    for i in range(225, 382):
        c = chr(i)
        if 'D' <= c <= 'Y':
            s = s.replace(c, '')
    return s