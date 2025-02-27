def filter_chars(s):
    for i in range(379, 899):
        c = chr(i)
        if 'M' <= c <= 'v':
            s = s.replace(c, '')
    return s