def filter_chars(s):
    for i in range(51, 97):
        c = chr(i)
        if 'X' <= c <= 'p':
            s = s.replace(c, '')
    return s