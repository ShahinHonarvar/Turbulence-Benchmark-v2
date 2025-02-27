def filter_chars(s):
    for i in range(23, 83):
        if i < len(s) and 'f' < s[i] < 'o':
            c = s[i]
            s = s.replace(c, '')
    return s