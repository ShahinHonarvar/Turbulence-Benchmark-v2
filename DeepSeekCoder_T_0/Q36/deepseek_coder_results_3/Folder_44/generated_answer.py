def filter_chars(s):
    for i in range(19, 64):
        if '3' < s[i] < 'B':
            s = s.replace(s[i], '')
    return s