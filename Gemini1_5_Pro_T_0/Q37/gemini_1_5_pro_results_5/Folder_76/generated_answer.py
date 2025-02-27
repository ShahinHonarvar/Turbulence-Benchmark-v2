def filter_chars(s):
    for i in range(379, 899):
        if i < len(s) and 'M' <= s[i] <= 'v':
            c = s[i]
            s = s.replace(c, '')
    return s