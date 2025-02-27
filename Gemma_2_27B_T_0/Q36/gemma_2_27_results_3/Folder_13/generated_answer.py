def filter_chars(s):
    for i in range(323, 526):
        c = s[i]
        if c > ')' and c < 'O':
            s = s.replace(c, '')
    return s