def filter_chars(s):
    for i in range(79, 81):
        c = s[i]
        if 'S' < c < '[':
            s = s.replace(c, '')
    return s