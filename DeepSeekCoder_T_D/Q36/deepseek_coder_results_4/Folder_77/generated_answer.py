def filter_chars(s):
    for i in range(222, 419):
        if '-' < s[i] < 'v':
            s = s.replace(s[i], '')
    return s