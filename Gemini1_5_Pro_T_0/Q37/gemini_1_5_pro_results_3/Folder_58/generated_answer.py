def filter_chars(s):
    for i in range(503, 754):
        if i < len(s) and '9' <= s[i] <= 'w':
            c = s[i]
            s = s.replace(c, '')
    return s