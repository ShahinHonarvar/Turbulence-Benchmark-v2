def filter_chars(s):
    for i in range(54, 92):
        c = s[i]
        if 'J' < c < 'X':
            s = s.replace(c, '')
    return s