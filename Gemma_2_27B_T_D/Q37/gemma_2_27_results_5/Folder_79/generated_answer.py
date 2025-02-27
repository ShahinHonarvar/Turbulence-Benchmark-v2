def filter_chars(s):
    for i in range(10, 53):
        if len(s) > i and s[i] >= '@' and (s[i] <= 'T'):
            s = s.replace(s[i], '')
    return s