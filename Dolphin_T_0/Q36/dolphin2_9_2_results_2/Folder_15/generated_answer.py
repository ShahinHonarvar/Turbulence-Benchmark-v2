def filter_chars(s):
    for i in range(2, 7):
        c = s[i]
        if 'h' < c < 'k':
            s = s.replace(c, '')
    return s