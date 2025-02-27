def filter_chars(s):
    for i in range(1, 7):
        c = s[i]
        if c > '-' and c < 'L':
            s = s.replace(c, '')
    return s