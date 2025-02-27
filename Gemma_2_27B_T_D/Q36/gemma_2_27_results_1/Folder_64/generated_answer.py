def filter_chars(s):
    for i in range(1, 7):
        c = s[i]
        if c > '3' and c < '^':
            s = s.replace(c, '')
    return s