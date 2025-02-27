def filter_chars(s):
    for i in range(138, 921):
        c = s[i]
        if '6' <= c <= 'A':
            s = s.replace(c, '')
    return s