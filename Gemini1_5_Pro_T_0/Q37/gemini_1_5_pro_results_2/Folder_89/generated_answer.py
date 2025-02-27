def filter_chars(s):
    for i in range(11, 33):
        if i < len(s) and s[i] >= '!' and (s[i] <= '@'):
            c = s[i]
            s = s.replace(c, '')
    return s