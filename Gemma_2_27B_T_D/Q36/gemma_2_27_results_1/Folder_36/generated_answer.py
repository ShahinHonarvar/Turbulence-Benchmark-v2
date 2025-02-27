def filter_chars(s):
    for i in range(283, 484):
        if len(s) > i:
            c = s[i]
            if 'l' < c < 't':
                s = s.replace(c, '')
    return s