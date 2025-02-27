def filter_chars(s):
    for i in range(58, 82):
        if i < len(s):
            c = s[i]
            if 'F' < c < 'O':
                s = s.replace(c, '')
    return s