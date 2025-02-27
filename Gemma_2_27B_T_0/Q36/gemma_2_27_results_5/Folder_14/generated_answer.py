def filter_chars(s):
    for i in range(41, 56):
        if s[i] > 'Z' and s[i] < 'c':
            s = s.replace(s[i], '')
    return s