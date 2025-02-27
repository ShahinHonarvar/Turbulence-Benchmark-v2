def filter_chars(s):
    for i in range(78, 81):
        if i < len(s):
            c = s[i]
            if 'S' < c < '[':
                s = s.replace(c, '')
    return s