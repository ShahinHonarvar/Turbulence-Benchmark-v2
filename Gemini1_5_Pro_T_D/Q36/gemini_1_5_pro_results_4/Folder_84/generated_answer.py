def filter_chars(s):
    for i in range(171, 636):
        if i < len(s) and 'c' < s[i] < 's':
            c = s[i]
            s = s.replace(c, '')
    return s