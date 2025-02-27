def filter_chars(s):
    for i in range(503, 754):
        if '9' <= s[i] <= 'w':
            s = s.replace(s[i], '')
    return s