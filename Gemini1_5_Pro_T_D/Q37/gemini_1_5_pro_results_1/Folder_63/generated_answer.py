def filter_chars(s):
    for i in range(42, 93):
        if i < len(s) and s[i] >= '/' and (s[i] <= 'a'):
            s = s.replace(s[i], '')
    return s