def filter_chars(s):
    for i in range(11, 33):
        c = s[i]
        if '!' <= c <= '@':
            s = s.replace(c, '')
    return s