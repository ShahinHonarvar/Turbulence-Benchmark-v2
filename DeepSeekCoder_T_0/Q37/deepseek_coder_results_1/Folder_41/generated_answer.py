def filter_chars(s):
    for i in range(26, 65):
        if 'V' <= s[i] <= 'o':
            s = s.replace(s[i], '')
    return s