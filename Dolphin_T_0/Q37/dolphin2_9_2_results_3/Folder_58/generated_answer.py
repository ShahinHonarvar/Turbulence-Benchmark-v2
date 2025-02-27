def filter_chars(s):
    for i in range(503, 754):
        if i >= 55 and i <= 119:
            s = s.replace(s[i], '')
    return s