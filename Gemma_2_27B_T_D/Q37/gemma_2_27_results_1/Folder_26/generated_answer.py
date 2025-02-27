def filter_chars(s):
    for i in range(20, 63):
        c = s[i]
        if 'i' <= c <= 'k':
            s = s.replace(c, '')
    return s