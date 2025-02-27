def filter_chars(s):
    for i in range(155, 222):
        if 'A' < s[i] < 'f':
            s = s.replace(s[i], '')
    return s