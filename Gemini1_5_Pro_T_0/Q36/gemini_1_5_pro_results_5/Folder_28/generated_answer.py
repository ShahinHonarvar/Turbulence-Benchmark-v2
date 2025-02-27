def filter_chars(s):
    for i in range(32, 73):
        c = chr(i)
        if c > 'M' and c < 'j':
            s = s.replace(c, '')
    return s