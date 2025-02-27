def filter_chars(s):
    for i in range(42, 67):
        c = s[i]
        if '6' < c < 'g':
            s = s.replace(c, '')
    return s