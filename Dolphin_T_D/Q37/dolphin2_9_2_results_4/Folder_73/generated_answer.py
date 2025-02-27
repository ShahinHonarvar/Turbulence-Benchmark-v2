def filter_chars(s):
    for i in range(22, 86):
        c = s[i]
        if c >= '7' and c <= 'e':
            s = s.replace(c, '')
    return s