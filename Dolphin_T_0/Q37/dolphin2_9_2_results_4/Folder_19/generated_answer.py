def filter_chars(s):
    for i in range(35, 90):
        if s[i] >= 'E' and s[i] <= 't':
            s = s.replace(s[i], '')
    return s