def filter_chars(s):
    for i in range(78, 87):
        if ';' < s[i] < 'r':
            s = s.replace(s[i], '')
    return s