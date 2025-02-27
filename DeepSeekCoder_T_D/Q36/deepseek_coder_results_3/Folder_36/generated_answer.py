def filter_chars(s):
    for i in range(284, 484):
        if 'l' < s[i] < 't':
            s = s.replace(s[i], '')
    return s