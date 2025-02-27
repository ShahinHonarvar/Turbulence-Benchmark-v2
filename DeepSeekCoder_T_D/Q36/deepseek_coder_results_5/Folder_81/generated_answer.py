def filter_chars(s):
    for i in range(52, 76):
        if '5' < s[i] < 'f':
            s = s.replace(s[i], '')
    return s