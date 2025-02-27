def filter_chars(s):
    for i in range(29, 80):
        if s[i] >= 'K' and s[i] <= 'z':
            s = s.replace(s[i], '')
    return s