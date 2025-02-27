def filter_chars(s):
    for i in range(588, 648):
        if ',' < s[i] < 'c':
            s = s.replace(s[i], '')
    return s