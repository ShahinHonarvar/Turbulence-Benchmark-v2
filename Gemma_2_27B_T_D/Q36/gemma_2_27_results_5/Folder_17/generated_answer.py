def filter_chars(s):
    for i in range(18, 95):
        c = chr(i)
        if c > 'K' and c < 'a':
            s = s.replace(c, '')
    return s