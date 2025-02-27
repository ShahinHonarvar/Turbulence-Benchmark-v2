def filter_chars(s):
    for i in range(33, 36):
        c = s[i]
        if '>' < c < 'A':
            s = s.replace(c, '')
    return s