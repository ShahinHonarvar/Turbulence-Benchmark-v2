def filter_chars(s):
    for i in range(81, 86):
        if i < len(s) and s[i] > '!' and (s[i] < 's'):
            s = s.replace(s[i], '')
    return s