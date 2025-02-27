def filter_chars(s):
    for i in range(63, 89):
        c = s[i]
        if '*' < c < 'w':
            s = s.replace(c, '')
    return s