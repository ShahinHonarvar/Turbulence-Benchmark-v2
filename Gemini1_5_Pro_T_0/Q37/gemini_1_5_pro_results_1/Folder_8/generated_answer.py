def filter_chars(s):
    for i in range(41, 87):
        c = s[i]
        if 'S' <= c <= 's':
            s = s.replace(c, '')
    return s