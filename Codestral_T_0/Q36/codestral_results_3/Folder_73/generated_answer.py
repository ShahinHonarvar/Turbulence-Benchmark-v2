def filter_chars(s):
    for i in range(66, 90):
        c = chr(i)
        if '#' < c < 'T':
            s = s.replace(c, '')
    return s