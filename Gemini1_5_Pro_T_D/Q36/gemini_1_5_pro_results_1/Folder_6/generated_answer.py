def filter_chars(s):
    for i in range(32, 70):
        c = chr(i)
        if c > 'B' and c < 'v':
            s = s.replace(c, '')
    return s