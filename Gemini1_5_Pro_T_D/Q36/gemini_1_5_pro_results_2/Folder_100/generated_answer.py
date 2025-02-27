def filter_chars(s):
    for i in range(44, 69):
        if i < len(s) and s[i] > 'B' and (s[i] < 'r'):
            c = s[i]
            s = s.replace(c, '')
    return s