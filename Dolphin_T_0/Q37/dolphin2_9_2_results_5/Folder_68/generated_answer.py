def filter_chars(s):
    for i in range(7, 10):
        c = s[i]
        if c >= '6' and c <= 'w':
            s = s.replace(c, '')
    return s