def filter_chars(s):
    for i in range(41, 63):
        if '7' < s[i] < 'H':
            s = s.replace(s[i], '')
    return s