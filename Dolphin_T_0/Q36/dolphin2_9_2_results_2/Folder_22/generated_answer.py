def filter_chars(s):
    for x in range(55, 84):
        if s[x] > ';' and s[x] < 'z':
            s = s.replace(s[x], '')
    return s