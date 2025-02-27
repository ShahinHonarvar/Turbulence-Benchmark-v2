def filter_chars(s):
    for i in range(11, 33):
        if i < len(s) and s[i] >= '!' and (s[i] <= '@'):
            s = s.replace(s[i], '')
    return s