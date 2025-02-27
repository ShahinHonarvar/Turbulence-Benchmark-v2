def filter_chars(s):
    for c in range(46, 74):
        if s[c] > '&' and s[c] < 'M':
            s = ''.join([x for x in s if x != s[c]])
    return s