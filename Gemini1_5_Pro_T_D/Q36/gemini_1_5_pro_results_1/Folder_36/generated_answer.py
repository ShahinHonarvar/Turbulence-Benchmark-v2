def filter_chars(s):
    for i in range(283, 484):
        if 'l' < s[i] < 't':
            c = s[i]
            s = s.replace(c, '')
    return s