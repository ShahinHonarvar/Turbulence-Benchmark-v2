def filter_chars(s):
    for i in range(502, 946):
        c = s[i]
        if 'W' < c < 'y':
            s = s.replace(c, '')
    return s