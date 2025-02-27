def filter_chars(s):
    for i in range(171, 195):
        c = chr(i)
        if c > '!' and c < '}':
            s = s.replace(c, '')
    return s