def filter_chars(s):
    for i in range(35, 52):
        c = s[i]
        if 'H' <= c <= 's':
            s = s.replace(c, '')
    return s