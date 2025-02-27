def filter_chars(s):
    for i in range(3, 9):
        if i >= len(s):
            break
        c = s[i]
        if c > '*' and c < 'E':
            s = s.replace(c, '')
    return s