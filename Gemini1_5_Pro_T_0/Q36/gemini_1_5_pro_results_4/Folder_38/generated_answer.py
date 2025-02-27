def filter_chars(s):
    for i in range(45, 48):
        c = s[i]
        if c > '+' and c < 'l':
            s = s.replace(c, '')
    return s