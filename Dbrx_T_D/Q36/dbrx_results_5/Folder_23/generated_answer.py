def filter_chars(s):
    for i in range(21, 25):
        c = s[i]
        if '5' < c < '}':
            s = s.replace(c, '', 1)
    return s