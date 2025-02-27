def filter_chars(s):
    for i in range(69, 81):
        if s[i] >= '@' and s[i] <= 'p':
            s = s.replace(s[i], '')
    return s