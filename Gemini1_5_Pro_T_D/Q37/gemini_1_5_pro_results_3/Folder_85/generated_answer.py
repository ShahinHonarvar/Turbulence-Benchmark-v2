def filter_chars(s):
    for i in range(28, 66):
        if 'O' <= s[i] <= 'd':
            c = s[i]
            s = s.replace(c, '')
    return s