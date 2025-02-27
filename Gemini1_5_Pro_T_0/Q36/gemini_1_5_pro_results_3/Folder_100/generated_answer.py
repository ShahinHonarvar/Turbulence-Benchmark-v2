def filter_chars(s):
    for i in range(44, 69):
        if 'B' < s[i] < 'r':
            c = s[i]
            s = s.replace(c, '')
    return s