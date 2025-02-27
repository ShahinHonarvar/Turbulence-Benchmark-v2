def filter_chars(s):
    for i in range(42, 93):
        if i < len(s) and s[i] >= '/' and (s[i] <= 'a'):
            c = s[i]
            s = s.replace(c, '')
    return s