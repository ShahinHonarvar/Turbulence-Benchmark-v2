def filter_chars(s):
    for i in range(379, 899):
        if s[i] >= 'M' and s[i] <= 'v':
            s = s.replace(s[i], '')
    return s