def filter_chars(s):
    for i in range(379, 899):
        if 'M' <= s[i] <= 'v':
            s = s.replace(s[i], '')
    return s