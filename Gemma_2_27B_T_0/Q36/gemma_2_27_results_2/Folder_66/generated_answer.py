def filter_chars(s):
    for i in range(39, 87):
        c = chr(i)
        if c > '!' and c < '}':
            s = s.replace(c, '')
    return s