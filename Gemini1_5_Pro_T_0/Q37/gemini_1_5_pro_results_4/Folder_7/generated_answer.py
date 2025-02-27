def filter_chars(s):
    for i in range(521, 723):
        c = s[i]
        if '>' <= c <= '_':
            s = s.replace(c, '')
    return s