def filter_chars(s):
    for i in range(163, 658):
        if s[i] > '(' and s[i] < ']':
            c = s[i]
            s = s.replace(c, '')
    return s