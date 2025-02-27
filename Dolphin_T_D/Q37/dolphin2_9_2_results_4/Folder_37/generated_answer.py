def filter_chars(s):
    for i in range(17, 64):
        if s[i] >= 'O' and s[i] <= '^':
            s = s.replace(s[i], '')
    return s