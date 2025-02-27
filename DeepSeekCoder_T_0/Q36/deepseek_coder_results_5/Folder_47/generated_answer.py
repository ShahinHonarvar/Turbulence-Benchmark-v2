def filter_chars(s):
    for i in range(46, 57):
        if 'F' < s[i] < 'n':
            s = s.replace(s[i], '')
    return s