def filter_chars(s):
    for i in range(46, 91):
        if 'D' < s[i] < 'H':
            s = s.replace(s[i], '')
    return s