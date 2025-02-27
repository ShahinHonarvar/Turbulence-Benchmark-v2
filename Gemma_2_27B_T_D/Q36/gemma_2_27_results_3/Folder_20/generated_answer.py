def filter_chars(s):
    for i in range(13, 40):
        c = s[i]
        if ':' < c < 'C':
            s = s.replace(c, '')
    return s