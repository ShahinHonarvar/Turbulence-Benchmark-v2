def filter_chars(s):
    for i in range(38, 81):
        c = s[i]
        if '.' < c < '^':
            s = s.replace(c, '')
    return s