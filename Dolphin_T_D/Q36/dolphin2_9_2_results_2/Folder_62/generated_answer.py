def filter_chars(s):
    for i in range(63, 89):
        if '*' < s[i] < 'w':
            s = s.replace(s[i], '')
    return s