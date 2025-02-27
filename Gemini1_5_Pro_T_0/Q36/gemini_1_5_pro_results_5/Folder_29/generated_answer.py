def filter_chars(s):
    for i in range(46, 68):
        if i >= len(s):
            break
        c = s[i]
        if 'H' < c < 's':
            s = s.replace(c, '')
    return s