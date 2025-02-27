def filter_chars(s):
    t = s[27:30]
    for i in range(len(t)):
        if ';' <= t[i] <= 'b':
            s = s.replace(t[i], '')
    return s