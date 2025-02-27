def filter_chars(s):
    for i in range(171, 636):
        if 'c' < s[i] < 's':
            s = s.replace(s[i], '')
    return s