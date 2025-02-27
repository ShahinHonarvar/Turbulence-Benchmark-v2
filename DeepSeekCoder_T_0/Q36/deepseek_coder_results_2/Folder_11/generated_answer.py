def filter_chars(s):
    for i in range(87, 93):
        if 'E' < s[i] < '~':
            s = s.replace(s[i], '')
    return s