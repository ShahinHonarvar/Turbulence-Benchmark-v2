def filter_chars(s):
    for i in range(17, 64):
        c = s[i]
        if 'O' <= c <= '^':
            s = s.replace(c, '')
    return s