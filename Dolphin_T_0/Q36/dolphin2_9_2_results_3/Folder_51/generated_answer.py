def filter_chars(s):
    for i in range(58, 81):
        c = s[i]
        if c > '5' and c < '>':
            s = s.replace(c, '')
    return s