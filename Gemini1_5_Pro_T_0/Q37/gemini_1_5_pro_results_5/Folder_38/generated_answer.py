def filter_chars(s):
    for i in range(24, 80):
        if i < len(s) and s[i] >= 'a' and (s[i] <= 'f'):
            c = s[i]
            s = s.replace(c, '')
    return s