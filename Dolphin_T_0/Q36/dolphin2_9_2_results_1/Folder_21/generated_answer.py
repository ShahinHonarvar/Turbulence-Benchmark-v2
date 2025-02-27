def filter_chars(s):
    for i in range(219, 403):
        c = s[i]
        if '*' < c < '7':
            s = s.replace(c, '')
    return s