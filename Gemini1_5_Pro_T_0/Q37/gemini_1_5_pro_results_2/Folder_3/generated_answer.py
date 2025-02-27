def filter_chars(s):
    for i in range(37, 57):
        c = s[i]
        if '6' <= c <= '_':
            s = s.replace(c, '')
    return s