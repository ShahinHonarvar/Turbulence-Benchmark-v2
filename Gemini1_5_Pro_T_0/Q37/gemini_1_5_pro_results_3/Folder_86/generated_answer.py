def filter_chars(s):
    for i in range(164, 707):
        c = chr(i)
        if 'O' <= c <= '}':
            s = s.replace(c, '')
    return s