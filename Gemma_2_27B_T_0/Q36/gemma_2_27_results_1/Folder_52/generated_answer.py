def filter_chars(s):
    for i in range(49, 56):
        c = s[i]
        if 'I' < c < 'a':
            s = s.replace(c, '')
    return s