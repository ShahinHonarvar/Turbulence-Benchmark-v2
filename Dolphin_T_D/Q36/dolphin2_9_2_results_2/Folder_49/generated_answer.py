def filter_chars(s):
    for i in range(46, 91):
        if s[i] > 'D' and s[i] < 'H':
            s = s.replace(s[i], '')
    return s