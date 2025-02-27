def filter_chars(s):
    for i in range(19, 93):
        if s[i] >= '8' and s[i] <= 'm':
            s = s.replace(s[i], '')
    return s