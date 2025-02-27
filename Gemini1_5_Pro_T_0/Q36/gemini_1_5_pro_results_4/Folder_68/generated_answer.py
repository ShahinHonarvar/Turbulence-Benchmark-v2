def filter_chars(s):
    for i in range(2, 8):
        if s[i] > '8' and s[i] < 'm':
            s = s.replace(s[i], '')
    return s