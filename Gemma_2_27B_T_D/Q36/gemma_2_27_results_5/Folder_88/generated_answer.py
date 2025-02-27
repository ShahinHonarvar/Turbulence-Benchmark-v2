def filter_chars(s):
    for i in range(78, 81):
        c = s[i]
        if c > 'S' and c < '[':
            s = s.replace(c, '')
    return s