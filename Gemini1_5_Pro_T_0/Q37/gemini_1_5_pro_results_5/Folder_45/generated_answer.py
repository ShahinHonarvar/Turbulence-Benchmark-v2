def filter_chars(s):
    for i in range(72, 95):
        c = chr(i)
        if '.' <= c <= 'b':
            s = s.replace(c, '')
    return s