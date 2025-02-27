def filter_chars(s):
    for i in range(669, 888):
        if 'B' < s[i] < 'Y':
            s = s.replace(s[i], '')
    return s