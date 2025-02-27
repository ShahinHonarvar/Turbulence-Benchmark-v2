def filter_chars(s):
    for i in range(69, 87):
        c = s[i]
        if s[i] > '#' and s[i] < 'L':
            s = s.replace(c, '')
    return s