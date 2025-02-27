def filter_chars(s):
    for i in range(170, 195):
        c = s[i]
        if '!' < c < '}':
            s = s.replace(c, '')
    return s