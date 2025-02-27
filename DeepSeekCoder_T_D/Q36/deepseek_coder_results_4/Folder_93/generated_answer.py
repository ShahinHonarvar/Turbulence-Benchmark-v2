def filter_chars(s):
    for i in range(53, 88):
        if '&' < s[i] < 'c':
            s = s.replace(s[i], '')
    return s