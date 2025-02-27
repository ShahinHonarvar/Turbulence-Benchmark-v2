def filter_chars(s):
    for i in range(71, 95):
        c = chr(i)
        if 'K' <= c <= 'a':
            s = s.replace(c, '')
    return s