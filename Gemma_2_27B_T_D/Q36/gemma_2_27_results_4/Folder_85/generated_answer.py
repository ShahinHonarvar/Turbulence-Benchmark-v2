def filter_chars(s):
    for i in range(55, 80):
        c = chr(i)
        if c > 'S' and c < 's':
            s = s.replace(c, '')
    return s