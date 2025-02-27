def filter_chars(s):
    for i in range(55, 84):
        if s[i] > ';' and s[i] < 'z':
            s = s.replace(s[i], '')
    return s