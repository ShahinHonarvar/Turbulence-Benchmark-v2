def filter_chars(s):
    for i in range(41, 56):
        c = s[i]
        if 'Z' < c < 'c':
            s = s.replace(c, '')
    return s