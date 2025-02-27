def filter_chars(s):
    for i in range(587, 648):
        if s[i] > ',' and s[i] < 'c':
            s = s.replace(s[i], '')
    return s