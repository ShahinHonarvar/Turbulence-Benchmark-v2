def filter_chars(s):
    for i in range(78, 87):
        if s[i] > ';' and s[i] < 'r':
            s = s.replace(s[i], '')
    return s