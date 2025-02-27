def filter_chars(s):
    for i in range(477, 948):
        if 'b' < s[i] < 'd':
            s = s.replace(s[i], '')
    return s