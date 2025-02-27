def filter_chars(s):
    for i in range(23, 45):
        if s[i] > '3' and s[i] < 'I':
            s = s.replace(s[i], '')
    return s