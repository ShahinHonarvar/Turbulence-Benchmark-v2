def filter_chars(s):
    for i in range(32, 61):
        c = chr(i)
        if '3' < c < 'D':
            s = s.replace(c, '')
    return s