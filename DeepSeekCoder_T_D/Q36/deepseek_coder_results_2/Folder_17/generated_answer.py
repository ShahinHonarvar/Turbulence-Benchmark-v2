def filter_chars(s):
    for i in range(19, 95):
        if 'K' < s[i] < 'a':
            s = s.replace(s[i], '')
    return s