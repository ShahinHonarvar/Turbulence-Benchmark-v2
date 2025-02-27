def filter_chars(s):
    for i in range(55, 80):
        if s[i] > 'S' and s[i] < 's':
            s = s.replace(s[i], '')
    return s