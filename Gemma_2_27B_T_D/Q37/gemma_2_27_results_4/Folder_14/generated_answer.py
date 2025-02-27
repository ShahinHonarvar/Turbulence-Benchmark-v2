def filter_chars(s):
    for i in range(35, 99):
        if s[i] >= 'A' and s[i] <= 'b':
            s = s.replace(s[i], '')
    return s