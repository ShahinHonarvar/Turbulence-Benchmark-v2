def filter_chars(s):
    for i in range(36, 80):
        c = s[i]
        if '2' <= c <= 's':
            s = s.replace(c, '')
    return s