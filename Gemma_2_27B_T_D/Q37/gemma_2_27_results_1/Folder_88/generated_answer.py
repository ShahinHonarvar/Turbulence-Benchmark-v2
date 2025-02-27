def filter_chars(s):
    for i in range(69, 81):
        if i < len(s):
            if s[i] >= '@' and s[i] <= 'p':
                s = s.replace(s[i], '')
    return s