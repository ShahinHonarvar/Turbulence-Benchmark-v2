def filter_chars(s):
    for i in range(14, 75):
        if '9' < s[i] < 'K':
            s = s.replace(s[i], '')
    return s