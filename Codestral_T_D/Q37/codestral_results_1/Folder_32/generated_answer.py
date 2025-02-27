def filter_chars(s):
    for i in range(23, 90):
        c = s[i]
        if 'w' <= c <= '{':
            s = s.replace(c, '')
    return s