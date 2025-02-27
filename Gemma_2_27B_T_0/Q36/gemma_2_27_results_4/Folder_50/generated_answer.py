def filter_chars(s):
    for i in range(61, 88):
        c = chr(i)
        if c > '%' and c < 'q':
            s = s.replace(c, '')
    return s