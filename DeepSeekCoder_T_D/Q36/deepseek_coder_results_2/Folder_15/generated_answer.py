def filter_chars(s):
    for i in range(3, 7):
        if 'h' < s[i] < 'k':
            s = s.replace(s[i], '')
    return s