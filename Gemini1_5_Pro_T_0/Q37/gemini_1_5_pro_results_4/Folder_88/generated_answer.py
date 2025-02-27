def filter_chars(s):
    for i in range(69, 81):
        if i < len(s) and '@' <= s[i] <= 'p':
            c = s[i]
            s = s.replace(c, '')
    return s