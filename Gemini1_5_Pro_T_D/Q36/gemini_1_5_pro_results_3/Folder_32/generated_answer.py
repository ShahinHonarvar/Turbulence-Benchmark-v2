def filter_chars(s):
    for i in range(40, 63):
        if i >= len(s):
            break
        if s[i] > '7' and s[i] < 'H':
            s = s.replace(s[i], '')
    return s