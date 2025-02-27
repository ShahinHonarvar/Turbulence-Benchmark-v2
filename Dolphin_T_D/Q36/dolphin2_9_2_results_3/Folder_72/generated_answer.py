def filter_chars(s):
    for i in range(44, 68):
        if 'W' < s[i] < 'x':
            return s.replace(s[i], '')
    return s