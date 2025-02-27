def filter_chars(s):
    for i in range(63, 89):
        ch = s[i]
        if '*' < ch < 'w':
            s = s.replace(ch, '')
    return s