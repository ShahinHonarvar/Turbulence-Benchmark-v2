def filter_chars(s):
    for i in range(32, 61):
        if s[i] > '3' and s[i] < 'D':
            s = s.replace(s[i], '')
    return s