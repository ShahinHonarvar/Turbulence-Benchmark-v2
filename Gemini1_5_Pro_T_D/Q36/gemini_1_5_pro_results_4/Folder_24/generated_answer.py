def filter_chars(s):
    for i in range(11, 15):
        if s[i] > 't' and s[i] < 'v':
            s = s.replace(s[i], '')
    return s