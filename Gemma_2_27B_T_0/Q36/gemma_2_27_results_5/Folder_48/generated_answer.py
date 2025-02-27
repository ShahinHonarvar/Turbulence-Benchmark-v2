def filter_chars(s):
    for i in range(154, 222):
        c = chr(i)
        if 'A' < c < 'f':
            s = s.replace(c, '')
    return s