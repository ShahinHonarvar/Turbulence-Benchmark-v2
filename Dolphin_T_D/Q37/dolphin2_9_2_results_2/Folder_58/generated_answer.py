def filter_chars(s):
    for i in range(503, 754):
        if s[i] >= '9' and s[i] <= 'w':
            s = s[:i] + s[i + 1:]
    return s