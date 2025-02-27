def filter_chars(s):
    for i in range(86, 93):
        c = chr(i)
        if c > 'E' and c < '~':
            s = s.replace(c, '')
    return s