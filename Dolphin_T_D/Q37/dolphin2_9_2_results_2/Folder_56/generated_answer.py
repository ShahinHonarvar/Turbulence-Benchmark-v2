def filter_chars(s):
    for i in range(71, 95):
        c = s[i]
        if c >= 'K' and c <= 'a':
            s = s.replace(c, '')
    return s