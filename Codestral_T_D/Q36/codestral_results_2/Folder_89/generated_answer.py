def filter_chars(s):
    for i in range(57, 69):
        if '(' < s[i] < 'W':
            s = s.replace(s[i], '')
    return s