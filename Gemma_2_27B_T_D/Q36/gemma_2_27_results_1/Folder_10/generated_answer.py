def filter_chars(s):
    for i in range(35, 60):
        c = s[i]
        if '!' < c < 'B':
            s = s.replace(c, '')
    return s