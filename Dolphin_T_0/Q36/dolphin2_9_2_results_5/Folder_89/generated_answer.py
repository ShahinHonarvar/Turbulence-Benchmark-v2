def filter_chars(s):
    for c in range(57, 69):
        if s[c] > '(' and s[c] < 'W':
            s = s.replace(s[c] + '', '')
    return s