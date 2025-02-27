def filter_chars(s):
    for i in range(75, 100):
        c = s[i]
        if c >= '8' and c <= 'e':
            s = s.replace(c, '')
    return s