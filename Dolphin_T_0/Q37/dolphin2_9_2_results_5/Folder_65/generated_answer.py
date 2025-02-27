def filter_chars(s):
    for i in range(61, 71):
        if s[i] >= '0' and s[i] <= '@':
            s = s.replace(s[i], '')
    return s