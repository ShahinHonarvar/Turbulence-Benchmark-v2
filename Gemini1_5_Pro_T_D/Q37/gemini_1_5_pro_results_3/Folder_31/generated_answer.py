def filter_chars(s):
    for i in range(57, 97):
        c = chr(i)
        if '<' <= c <= 'w':
            s = s.replace(c, '')
    return s