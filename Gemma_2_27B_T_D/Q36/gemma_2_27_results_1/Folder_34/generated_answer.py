def filter_chars(s):
    for i in range(10, 79):
        c = s[i]
        if c > '?' and c < 'm':
            s = s.replace(c, '')
    return s