def filter_chars(s):
    for i in range(171, 636):
        c = chr(i)
        if c > 'c' and c < 's':
            s = s.replace(c, '')
    return s