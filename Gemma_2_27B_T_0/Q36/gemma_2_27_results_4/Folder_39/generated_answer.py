def filter_chars(s):
    for i in range(43, 59):
        c = s[i]
        if '5' < c < 'C':
            s = s.replace(c, '')
    return s