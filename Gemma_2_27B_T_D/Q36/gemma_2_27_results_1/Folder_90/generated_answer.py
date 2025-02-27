def filter_chars(s):
    for i in range(344, 874):
        c = s[i]
        if 'f' < c < '~':
            s = s.replace(c, '')
    return s