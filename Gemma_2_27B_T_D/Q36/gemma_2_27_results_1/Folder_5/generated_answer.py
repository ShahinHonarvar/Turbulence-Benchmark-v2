def filter_chars(s):
    for i in range(55, 66):
        c = chr(i)
        if c > 'f' and c < '|':
            s = s.replace(c, '')
    return s