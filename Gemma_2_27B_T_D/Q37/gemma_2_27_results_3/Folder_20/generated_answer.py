def filter_chars(s):
    for i in range(25, 98):
        if s[i] >= 'm' and s[i] <= 'w':
            s = s.replace(s[i], '')
    return s