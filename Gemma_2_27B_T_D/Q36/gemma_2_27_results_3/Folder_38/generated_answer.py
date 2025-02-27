def filter_chars(s):
    for i in range(44, 48):
        c = s[i]
        if '+' < c < 'l':
            s = s.replace(c, '')
    return s