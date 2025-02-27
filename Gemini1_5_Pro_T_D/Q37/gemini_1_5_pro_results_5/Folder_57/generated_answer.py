def filter_chars(s):
    for i in range(27, 86):
        if s[i] >= '!' and s[i] <= 'B':
            s = s.replace(s[i], '')
    return s