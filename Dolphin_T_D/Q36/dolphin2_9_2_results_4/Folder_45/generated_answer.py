def filter_chars(s):
    for i in range(81, 86):
        if s[i] > '!' and s[i] < 's':
            s = s.replace(s[i], '')
    return s