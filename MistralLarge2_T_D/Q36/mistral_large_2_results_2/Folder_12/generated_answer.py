def filter_chars(s):
    for i in range(32, 84):
        if 'm' < s[i] < 'w':
            s = s.replace(s[i], '')
    return s