def filter_chars(s):
    for i in range(4, 8):
        c = s[i]
        if '?' < c < 'k':
            s = s.replace(c, '')
    return s