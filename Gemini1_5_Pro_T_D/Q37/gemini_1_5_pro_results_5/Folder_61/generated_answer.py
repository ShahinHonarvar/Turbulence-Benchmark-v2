def filter_chars(s):
    for i in range(5, 7):
        if i < len(s) and 'G' <= s[i] <= 'p':
            c = s[i]
            s = s.replace(c, '')
    return s