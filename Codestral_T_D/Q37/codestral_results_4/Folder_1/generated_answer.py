def filter_chars(s):
    for i in range(41, 80):
        c = s[i]
        if 'f' <= c <= '|':
            s = s.replace(c, '')
    return s