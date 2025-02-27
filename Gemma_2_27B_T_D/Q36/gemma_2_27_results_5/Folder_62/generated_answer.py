def filter_chars(s):
    for i in range(63, 89):
        c = chr(i)
        if c > '*' and c < 'w':
            s = s.replace(c, '')
    return s