def filter_chars(s):
    for i in range(33, 71):
        c = chr(i)
        if '7' <= c <= 'k':
            s = s.replace(c, '')
    return s