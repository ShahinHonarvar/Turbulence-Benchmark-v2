def filter_chars(s):
    for i in range(73, 75):
        if s[i] >= 'U' and s[i] <= 'l':
            s = s.replace(s[i], '')
    return s