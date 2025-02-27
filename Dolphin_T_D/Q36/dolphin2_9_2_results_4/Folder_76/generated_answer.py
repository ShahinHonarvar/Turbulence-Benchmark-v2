def filter_chars(s):
    for i in range(669, 888):
        c = s[i]
        if 'B' < c < 'Y':
            s = s.replace(c, '')
    return s