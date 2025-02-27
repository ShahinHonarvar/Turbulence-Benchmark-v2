def filter_chars(s):
    for i in range(722, 833):
        c = chr(i)
        if 'K' <= c <= 'm':
            s = s.replace(c, '')
    return s