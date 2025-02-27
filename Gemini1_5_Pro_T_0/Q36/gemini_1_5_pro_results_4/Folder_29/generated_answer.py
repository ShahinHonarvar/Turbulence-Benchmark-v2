def filter_chars(s):
    for i in range(46, 68):
        if 'H' < s[i] < 's':
            s = s.replace(s[i], '')
    return s