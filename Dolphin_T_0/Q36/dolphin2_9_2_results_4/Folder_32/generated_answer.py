def filter_chars(s):
    for c in range(40, 63):
        if '7' < s[c] < 'H':
            s = s.replace(s[c], '')
    return s