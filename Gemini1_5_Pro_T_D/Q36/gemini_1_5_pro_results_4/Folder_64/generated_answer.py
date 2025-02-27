def filter_chars(s):
    for i in range(2, 6):
        if s[i] > '3' and s[i] < '^':
            s = s.replace(s[i], '')
    return s