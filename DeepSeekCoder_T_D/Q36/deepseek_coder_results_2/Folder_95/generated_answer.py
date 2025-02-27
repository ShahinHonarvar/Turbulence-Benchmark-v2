def filter_chars(s):
    for i in range(57, 86):
        if '+' < s[i] < 'w':
            s = s.replace(s[i], '')
    return s