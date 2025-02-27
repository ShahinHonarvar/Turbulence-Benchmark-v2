def filter_chars(s):
    for i in range(44, 68):
        c = s[i]
        if c > 'W' and c < 'x':
            s = s.replace(c, '')
    return s