def filter_chars(s):
    for i in range(31, 73):
        c = s[i]
        if 'M' < c < 'j':
            s = s.replace(c, '')
    return s