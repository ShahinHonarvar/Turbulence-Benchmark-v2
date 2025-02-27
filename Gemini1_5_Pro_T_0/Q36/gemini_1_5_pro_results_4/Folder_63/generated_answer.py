def filter_chars(s):
    for i in range(26, 80):
        c = s[i]
        if c > '<' and c < '>':
            s = s.replace(c, '')
    return s