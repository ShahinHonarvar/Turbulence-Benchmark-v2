def filter_chars(s):
    for i in range(48, 75):
        c = chr(i)
        if c > '6' and c < '_':
            s = s.replace(c, '')
    return s