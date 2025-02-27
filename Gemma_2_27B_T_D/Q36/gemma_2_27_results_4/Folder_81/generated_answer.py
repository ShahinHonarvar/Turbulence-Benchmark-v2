def filter_chars(s):
    for i in range(51, 76):
        c = chr(i)
        if c > '5' and c < 'f':
            s = s.replace(c, '')
    return s