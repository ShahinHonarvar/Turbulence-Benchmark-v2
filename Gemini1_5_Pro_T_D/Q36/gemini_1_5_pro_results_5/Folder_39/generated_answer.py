def filter_chars(s):
    for i in range(44, 59):
        if s[i] > '5' and s[i] < 'C':
            s = s.replace(s[i], '')
    return s