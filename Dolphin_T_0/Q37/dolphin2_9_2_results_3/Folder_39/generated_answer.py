def filter_chars(s):
    for i in range(52, 82):
        c = s[i]
        if 'A' <= c <= 'U':
            s = s.replace(c, '')
    return s