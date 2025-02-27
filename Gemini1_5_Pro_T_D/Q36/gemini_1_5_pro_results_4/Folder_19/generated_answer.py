def filter_chars(s):
    for i in range(78, 87):
        if s[i] > ';' and s[i] < 'r':
            c = s[i]
            s = s.replace(c, '')
    return s