def filter_chars(s):
    for i in range(4, 5):
        c = s[i]
        if '7' <= c <= 'o':
            s = s.replace(c, '')
    return s