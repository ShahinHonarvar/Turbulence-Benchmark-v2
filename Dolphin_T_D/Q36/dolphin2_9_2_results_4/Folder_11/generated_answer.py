def filter_chars(s):
    for i in range(86, 93):
        c = s[i]
        if 'E' < c and c < '~':
            s = s.replace(c, '')
    return s