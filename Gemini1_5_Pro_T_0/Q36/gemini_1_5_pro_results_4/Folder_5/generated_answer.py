def filter_chars(s):
    for i in range(55, 66):
        if i >= len(s):
            break
        c = s[i]
        if 'f' < c < '|':
            s = s.replace(c, '')
    return s