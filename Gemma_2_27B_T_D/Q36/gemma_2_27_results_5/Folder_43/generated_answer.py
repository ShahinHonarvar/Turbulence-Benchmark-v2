def filter_chars(s):
    for i in range(27, 75):
        if s[i] > 'A' and s[i] < 'i':
            s = s.replace(s[i], '')
    return s