def filter_chars(s):
    for i in range(19, 34):
        c = s[i]
        if 'S' <= c <= '{':
            s = s.replace(c, '')
    return s