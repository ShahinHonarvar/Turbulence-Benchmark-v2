def filter_chars(s):
    for i in range(587, 648):
        if i < len(s) and ',' < s[i] < 'c':
            c = s[i]
            s = s.replace(c, '')
    return s