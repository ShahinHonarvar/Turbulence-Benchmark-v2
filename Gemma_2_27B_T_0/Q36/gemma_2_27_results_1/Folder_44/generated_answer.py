def filter_chars(s):
    for i in range(18, 64):
        if s[i] > '3' and s[i] < 'B':
            s = s.replace(s[i], '')
    return s