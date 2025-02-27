def filter_chars(s):
    for i in range(56, 66):
        if i < len(s) and 'f' < s[i] < '|':
            c = s[i]
            s = s.replace(c, '')
    return s