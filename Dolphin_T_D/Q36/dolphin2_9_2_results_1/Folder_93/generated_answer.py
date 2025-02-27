def filter_chars(s):
    for i in range(52, 88):
        c = s[i]
        if '&' < c < 'c':
            s = s.replace(c, '')
    return s