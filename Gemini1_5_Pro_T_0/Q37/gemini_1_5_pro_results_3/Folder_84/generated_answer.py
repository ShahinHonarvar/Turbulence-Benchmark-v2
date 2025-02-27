def filter_chars(s):
    for i in range(138, 921):
        if i < len(s) and '6' <= s[i] <= 'A':
            c = s[i]
            s = s.replace(c, '')
    return s