def filter_chars(s):
    for i in range(51, 91):
        c = chr(i)
        if c > 'A' and c < 'Q':
            s = s.replace(c, '')
    return s