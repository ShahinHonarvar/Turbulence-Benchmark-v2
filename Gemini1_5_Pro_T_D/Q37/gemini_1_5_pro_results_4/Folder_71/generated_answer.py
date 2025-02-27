def filter_chars(s):
    for i in range(32, 47):
        c = chr(i)
        if '0' <= c <= 'k':
            s = s.replace(c, '')
    return s