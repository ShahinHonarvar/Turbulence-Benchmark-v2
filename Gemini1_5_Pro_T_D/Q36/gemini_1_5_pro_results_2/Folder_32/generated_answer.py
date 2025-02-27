def filter_chars(s):
    for i in range(40, 63):
        if i < len(s) and '7' < s[i] < 'H':
            c = s[i]
            s = s.replace(c, '')
    return s