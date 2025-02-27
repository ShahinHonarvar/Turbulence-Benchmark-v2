def filter_chars(s):
    for i in range(309, 591):
        if 'S' < s[i] < 'm':
            s = s.replace(s[i], '')
    return s