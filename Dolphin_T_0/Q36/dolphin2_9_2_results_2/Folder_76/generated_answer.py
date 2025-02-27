def filter_chars(s):
    for i in range(669, 888):
        if 'A' < s[i] < 'Y':
            s = s.replace(s[i], '')
    return s