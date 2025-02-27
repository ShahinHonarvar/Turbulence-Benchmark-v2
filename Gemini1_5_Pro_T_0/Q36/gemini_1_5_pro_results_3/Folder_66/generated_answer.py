def filter_chars(s):
    for i in range(39, 87):
        c = s[i]
        if '!' < c < '}':
            s = s.replace(c, '')
    return s