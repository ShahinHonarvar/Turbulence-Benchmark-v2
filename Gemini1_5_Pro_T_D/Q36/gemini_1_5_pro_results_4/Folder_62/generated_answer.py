def filter_chars(s):
    for i in range(63, 89):
        if i < len(s) and '*' < s[i] < 'w':
            c = s[i]
            s = s.replace(c, '')
    return s