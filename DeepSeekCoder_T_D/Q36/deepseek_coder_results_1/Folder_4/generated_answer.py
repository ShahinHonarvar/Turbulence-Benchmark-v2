def filter_chars(s):
    for i in range(43, 67):
        if '6' < s[i] < 'g':
            s = s.replace(s[i], '')
    return s