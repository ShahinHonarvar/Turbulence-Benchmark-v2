def filter_chars(s):
    for i in range(171, 636):
        if s[i] > 'c' and s[i] < 's':
            s = s.replace(s[i], '')
    return s