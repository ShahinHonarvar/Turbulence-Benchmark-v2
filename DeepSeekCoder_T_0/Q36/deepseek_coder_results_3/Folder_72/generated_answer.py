def filter_chars(s):
    for i in range(45, 68):
        if 'W' < s[i] < 'x':
            s = s.replace(s[i], '')
    return s