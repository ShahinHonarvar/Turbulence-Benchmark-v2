def filter_chars(s):
    for i in range(476, 948):
        if len(s) > i and 'b' < s[i] < 'd':
            s = s.replace(s[i], '')
    return s