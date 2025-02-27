def filter_chars(s):
    for i in range(477, 948):
        if s[i] > 'b' and s[i] < 'd':
            s = s.replace(s[i], '')
    return s