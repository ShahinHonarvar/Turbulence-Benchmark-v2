def filter_chars(s):
    for i in range(19, 93):
        if '8' <= s[i] <= 'm':
            s = s.replace(s[i], '')
    return s