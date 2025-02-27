def filter_chars(s):
    for i in range(10, 15):
        if i < len(s) and 't' < s[i] < 'v':
            c = s[i]
            s = s.replace(c, '')
    return s