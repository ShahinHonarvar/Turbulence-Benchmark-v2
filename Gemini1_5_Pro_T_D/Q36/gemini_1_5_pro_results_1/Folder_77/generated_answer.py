def filter_chars(s):
    for i in range(221, 419):
        c = s[i]
        if c > '-' and c < 'v':
            s = s.replace(c, '')
    return s