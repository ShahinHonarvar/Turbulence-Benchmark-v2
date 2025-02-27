def filter_chars(s):
    for i in range(18, 31):
        c = s[i]
        if 'H' < c < '|':
            s = s.replace(c, '')
    return s