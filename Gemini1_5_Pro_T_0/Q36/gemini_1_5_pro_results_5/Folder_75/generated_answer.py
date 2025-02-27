def filter_chars(s):
    for i in range(46, 74):
        if i < len(s) and '&' < s[i] < 'M':
            c = s[i]
            s = s.replace(c, '')
    return s