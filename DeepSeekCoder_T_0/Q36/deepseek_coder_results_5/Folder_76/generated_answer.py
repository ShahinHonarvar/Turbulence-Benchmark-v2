def filter_chars(s):
    for i in range(670, 888):
        if 'B' < s[i] < 'Y':
            s = s.replace(s[i], '')
    return s