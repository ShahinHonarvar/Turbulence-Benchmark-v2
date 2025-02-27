def filter_chars(s):
    for i in range(52, 88):
        if i < len(s) and s[i] > '&' and (s[i] < 'c'):
            c = s[i]
            s = s.replace(c, '')
    return s