def filter_chars(s):
    for i in range(83, 100):
        c = s[i]
        if '*' <= c <= 'j':
            s = s.replace(c, '')
    return s