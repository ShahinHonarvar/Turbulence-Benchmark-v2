def filter_chars(s):
    for i in range(10, 79):
        if i < len(s) and s[i] > '?' and (s[i] < 'm'):
            c = s[i]
            s = s.replace(c, '')
    return s