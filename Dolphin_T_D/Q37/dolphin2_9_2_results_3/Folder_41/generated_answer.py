def filter_chars(s):
    for i in range(26, 65):
        if s[i] >= 'V' and s[i] <= 'o':
            s = s.replace(s[i], '')
    return s