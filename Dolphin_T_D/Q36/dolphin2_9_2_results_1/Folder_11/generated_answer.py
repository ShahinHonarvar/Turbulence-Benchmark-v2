def filter_chars(s):
    for i in range(86, 93):
        if 'E' < s[i] < '~':
            s = s.replace(s[i], '')
    return s