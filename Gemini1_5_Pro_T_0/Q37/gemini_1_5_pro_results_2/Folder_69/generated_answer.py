def filter_chars(s):
    for i in range(114, 640):
        c = chr(i)
        if '!' <= c <= 'x':
            s = s.replace(c, '')
    return s