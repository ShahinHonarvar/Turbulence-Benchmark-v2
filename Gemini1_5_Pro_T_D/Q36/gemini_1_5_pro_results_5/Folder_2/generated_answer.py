def filter_chars(s):
    for i in range(421, 854):
        if 'D' < s[i] < 'J':
            c = s[i]
            s = s.replace(c, '')
    return s