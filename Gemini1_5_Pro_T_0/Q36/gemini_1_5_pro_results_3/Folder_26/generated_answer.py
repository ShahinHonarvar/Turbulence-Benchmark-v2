def filter_chars(s):
    for i in range(44, 83):
        if s[i] > ':' and s[i] < 'Q':
            s = s.replace(s[i], '')
    return s