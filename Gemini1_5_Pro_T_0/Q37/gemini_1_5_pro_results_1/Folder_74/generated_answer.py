def filter_chars(s):
    for i in range(19, 33):
        if i < len(s) and 'f' <= s[i] <= 'o':
            c = s[i]
            s = s.replace(c, '')
    return s