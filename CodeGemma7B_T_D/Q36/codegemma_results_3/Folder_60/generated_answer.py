def filter_chars(s):
    for i in range(23, 83):
        if s[i] > 'f' and s[i] < 'o':
            s = s.replace(s[i], '')
    return s