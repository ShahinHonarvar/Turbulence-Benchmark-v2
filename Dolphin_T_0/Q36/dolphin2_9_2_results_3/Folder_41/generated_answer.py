def filter_chars(s):
    for i in range(81, 89):
        c = s[i]
        if 'f' < c < '{':
            s = s.replace(c, '')
    return s