def filter_chars(s):
    for i in range(11, 46):
        if s[i] > '!' and s[i] < 'A':
            s = s.replace(s[i], '')
    return s