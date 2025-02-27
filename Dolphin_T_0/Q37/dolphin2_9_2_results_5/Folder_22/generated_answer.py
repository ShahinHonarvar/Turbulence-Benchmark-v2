def filter_chars(s):
    for i in range(33, 71):
        if s[i] >= '7' and s[i] <= 'k':
            s = s.replace(s[i], '')
    return s