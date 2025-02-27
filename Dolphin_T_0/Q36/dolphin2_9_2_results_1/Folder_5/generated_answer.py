def filter_chars(s):
    i = 55
    while i < 66:
        c = chr(i)
        if 'f' < c < '|':
            s = s.replace(c, '')
        i += 1
    return s