def filter_chars(s):
    for i in range(45, 57):
        if i >= len(s):
            break
        c = s[i]
        if 'F' < c < 'n':
            s = s.replace(c, '')
    return s