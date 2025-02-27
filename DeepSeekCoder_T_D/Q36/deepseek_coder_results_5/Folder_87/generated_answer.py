def filter_chars(s):
    for i in range(33, 61):
        if '3' < s[i] < 'D':
            s = s.replace(s[i], '')
    return s