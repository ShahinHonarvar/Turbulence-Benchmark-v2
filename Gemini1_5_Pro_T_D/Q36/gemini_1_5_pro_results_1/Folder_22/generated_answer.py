def filter_chars(s):
    for i in range(55, 84):
        if i < len(s) and ';' < s[i] < 'z':
            s = s.replace(s[i], '')
    return s