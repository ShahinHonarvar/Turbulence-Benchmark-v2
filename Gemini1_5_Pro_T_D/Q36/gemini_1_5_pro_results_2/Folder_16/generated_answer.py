def filter_chars(s):
    for i in range(332, 713):
        c = s[i]
        if 'M' < c < '_':
            s = s.replace(c, '')
    return s