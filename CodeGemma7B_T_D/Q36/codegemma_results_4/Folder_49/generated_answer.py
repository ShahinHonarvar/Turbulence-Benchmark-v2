def filter_chars(s):
    for i in range(46, 91):
        c = chr(i)
        if c > 'D' and c < 'H':
            while c in s:
                s = s.replace(c, '', 1)
    return s