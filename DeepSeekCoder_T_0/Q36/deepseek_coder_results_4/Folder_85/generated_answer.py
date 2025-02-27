def filter_chars(s):
    for i in range(56, 80):
        if 'S' < s[i] < 's':
            s = s.replace(s[i], '')
    return s