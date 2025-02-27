def filter_chars(s):
    for i in range(56, 86):
        if i < len(s) and '+' < s[i] < 'w':
            c = s[i]
            s = s.replace(c, '')
    return s