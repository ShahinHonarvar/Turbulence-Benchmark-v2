def filter_chars(s):
    for i in range(29, 80, 1):
        if 'K' <= s[i] <= 'z':
            s = s.replace(s[i], '')
    return s