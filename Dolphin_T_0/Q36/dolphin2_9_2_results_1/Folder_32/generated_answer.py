def filter_chars(s):
    to_remove = {chr(i) for i in range(65, 72)}
    for i in range(40, 63):
        c = s[i]
        if '7' < c < 'H':
            s = s.replace(c, '')
    return s