def filter_chars(s):
    for i in range(82, 89):
        c = s[i]
        if '*' < c < '[':
            s = s.replace(c, '')
    return s