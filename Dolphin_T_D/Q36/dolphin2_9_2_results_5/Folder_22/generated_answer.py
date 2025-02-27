def filter_chars(s):
    for c in range(55, 84):
        if ';' < s[c] < 'z':
            s = s.replace(s[c], '')
    return s