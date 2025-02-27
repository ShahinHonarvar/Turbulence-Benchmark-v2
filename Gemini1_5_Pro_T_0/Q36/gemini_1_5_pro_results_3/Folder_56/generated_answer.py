def filter_chars(s):
    for i in range(32, 49):
        c = chr(i)
        if c > '/' and c < 'J':
            s = s.replace(c, '')
    return s