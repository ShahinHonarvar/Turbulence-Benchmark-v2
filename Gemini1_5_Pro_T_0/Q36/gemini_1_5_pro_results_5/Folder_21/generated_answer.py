def filter_chars(s):
    for i in range(219, 403):
        c = chr(i)
        if c > '*' and c < '7':
            s = s.replace(c, '')
    return s