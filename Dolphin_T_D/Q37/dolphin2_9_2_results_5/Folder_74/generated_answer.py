def filter_chars(s):
    for i in range(19, 33):
        c = s[i]
        if c >= 'f' and c <= 'o':
            s = s.replace(c, '')
    return s