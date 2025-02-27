def filter_chars(s):
    for i in range(86, 93):
        if i >= len(s):
            break
        c = s[i]
        if 'E' < c < '~':
            s = s.replace(c, '')
    return s