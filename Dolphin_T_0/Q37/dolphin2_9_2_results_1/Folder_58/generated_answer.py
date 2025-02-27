def filter_chars(s):
    for i in range(503, 754):
        c = s[i]
        if c >= '9' and c <= 'w':
            s = s.replace(c, '')
    return s