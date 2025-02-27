def filter_chars(s):
    for i in range(72, 93):
        c = s[i]
        if '<' < c < 'J':
            s = s.replace(c, '')
    return s