def filter_chars(s):
    for i in range(43, 68):
        if s[i] > 't' and s[i] < 'x':
            s = s.replace(s[i], '')
    return s