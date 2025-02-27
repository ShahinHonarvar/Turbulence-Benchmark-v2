def filter_chars(s):
    for i in range(55, 80):
        if i < len(s) and 'S' < s[i] < 's':
            c = s[i]
            s = s.replace(c, '')
    return s