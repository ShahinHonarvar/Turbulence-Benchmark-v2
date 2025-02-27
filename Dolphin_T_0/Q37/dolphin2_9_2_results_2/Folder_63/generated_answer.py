def filter_chars(s):
    for i in range(42, 93):
        c = s[i]
        if c >= '/' and c <= 'a':
            s = s.replace(c, '')
    return s