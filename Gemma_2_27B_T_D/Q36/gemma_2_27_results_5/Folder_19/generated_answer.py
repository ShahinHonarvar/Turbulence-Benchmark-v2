def filter_chars(s):
    for i in range(77, 87):
        c = chr(i)
        if c > ';' and c < 'r':
            s = s.replace(c, '')
    return s