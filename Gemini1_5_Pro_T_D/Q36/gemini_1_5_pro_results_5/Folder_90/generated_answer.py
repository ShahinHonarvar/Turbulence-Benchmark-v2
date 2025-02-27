def filter_chars(s):
    for i in range(344, 874):
        if i < len(s) and 'f' < s[i] < '~':
            c = s[i]
            s = s.replace(c, '')
    return s