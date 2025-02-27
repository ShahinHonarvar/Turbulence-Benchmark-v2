def filter_chars(s):
    for i in range(332, 713):
        if s[i] > 'M' and s[i] < '_':
            s = s.replace(s[i], '')
    return s