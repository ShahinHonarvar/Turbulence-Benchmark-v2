def filter_chars(s):
    for i in range(164, 658):
        c = s[i]
        if c > '(' and c < ']':
            s = s.replace(c, '')
    return s