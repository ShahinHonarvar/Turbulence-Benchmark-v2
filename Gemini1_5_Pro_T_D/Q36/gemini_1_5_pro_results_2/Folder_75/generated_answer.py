def filter_chars(s):
    for i in range(46, 74):
        if i >= len(s):
            break
        c = s[i]
        if c > '&' and c < 'M':
            s = s.replace(c, '')
    return s