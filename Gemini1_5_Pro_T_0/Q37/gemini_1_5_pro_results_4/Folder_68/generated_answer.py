def filter_chars(s):
    for i in range(7, 10):
        if i < len(s) and '6' <= s[i] <= 'w':
            c = s[i]
            s = s.replace(c, '')
    return s