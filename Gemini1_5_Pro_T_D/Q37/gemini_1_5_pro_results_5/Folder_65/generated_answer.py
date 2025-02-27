def filter_chars(s):
    for i in range(61, 71):
        if i < len(s) and s[i] >= '0' and (s[i] <= '@'):
            c = s[i]
            s = s.replace(c, '')
    return s