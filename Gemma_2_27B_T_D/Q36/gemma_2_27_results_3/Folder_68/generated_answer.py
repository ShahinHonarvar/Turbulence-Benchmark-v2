def filter_chars(s):
    for i in range(1, 9):
        c = s[i]
        if '8' < c < 'm':
            s = s.replace(c, '')
    return s