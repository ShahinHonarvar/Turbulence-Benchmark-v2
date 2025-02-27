def filter_chars(s):
    for i in range(45, 59):
        c = s[i]
        if c > '/' and c < '6':
            s = s.replace(c, '')
    return s