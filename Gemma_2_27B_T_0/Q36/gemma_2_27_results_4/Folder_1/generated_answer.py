def filter_chars(s):
    for i in range(69, 87):
        c = chr(i)
        if c > '#' and c < 'L':
            s = s.replace(c, '')
    return s