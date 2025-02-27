def filter_chars(s):
    for i in range(323, 526):
        if i < len(s):
            c = s[i]
            if ')' < c < 'O':
                s = s.replace(c, '')
    return s