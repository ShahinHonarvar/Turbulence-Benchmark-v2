def filter_chars(s):
    for i in range(283, 484):
        if s[i] > 'l' and s[i] < 't':
            s = s.replace(s[i], '')
    return s