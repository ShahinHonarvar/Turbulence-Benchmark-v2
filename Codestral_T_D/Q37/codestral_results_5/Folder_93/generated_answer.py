def filter_chars(s):
    for i in range(38, 70):
        c = s[i]
        if 'H' <= c <= 'e':
            s = s.replace(c, '')
    return s