def filter_chars(s):
    for i in range(56, 84):
        if ';' < s[i] < 'z':
            s = s.replace(s[i], '')
    return s