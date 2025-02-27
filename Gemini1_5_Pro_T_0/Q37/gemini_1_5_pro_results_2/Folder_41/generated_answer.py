def filter_chars(s):
    for i in range(26, 65):
        c = chr(i)
        if 'V' <= c <= 'o':
            s = s.replace(c, '')
    return s