def filter_chars(s):
    for i in range(54, 92):
        if 'J' < s[i] < 'X':
            c = s[i]
            s = s.replace(c, '')
    return s