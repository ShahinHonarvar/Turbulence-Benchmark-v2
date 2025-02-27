def filter_chars(s):
    for i in range(19, 91):
        if s[i] >= 'F' and s[i] <= 'h':
            s = s.replace(s[i], '')
    return s