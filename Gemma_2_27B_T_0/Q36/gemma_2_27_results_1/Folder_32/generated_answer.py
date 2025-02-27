def filter_chars(s):
    for i in range(40, 63):
        c = chr(i)
        if c > '7' and c < 'H':
            s = s.replace(c, '')
    return s