def filter_chars(s):
    for i in range(163, 658):
        c = s[i]
        if '(' < c < ']':
            s = s.replace(c, '')
    return s