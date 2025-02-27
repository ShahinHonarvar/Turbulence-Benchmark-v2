def filter_chars(s):
    for i in range(172, 636):
        if 'c' < s[i] < 's':
            s = s.replace(s[i], '')
    return s