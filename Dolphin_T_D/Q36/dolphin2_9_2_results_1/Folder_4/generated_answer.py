def filter_chars(s):
    for i in range(42, 67):
        if s[i] > '6' and s[i] < 'g':
            s = s.replace(s[i], '')
    return s