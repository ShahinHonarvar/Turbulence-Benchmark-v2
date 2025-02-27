def filter_chars(s):
    for i in range(19, 69):
        c = s[i]
        if c > '<' and c < 'C':
            s = s.replace(c, '')
    return s