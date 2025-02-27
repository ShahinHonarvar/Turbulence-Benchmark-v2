def filter_chars(s):
    for i in range(41, 65):
        c = chr(i)
        if 'K' <= c <= ']':
            s = s.replace(c, '')
    return s