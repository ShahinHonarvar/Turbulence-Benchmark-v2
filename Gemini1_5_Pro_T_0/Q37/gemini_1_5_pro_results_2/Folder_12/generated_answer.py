def filter_chars(s):
    for i in range(19, 91):
        if i < len(s) and 'F' <= s[i] <= 'h':
            c = s[i]
            s = s.replace(c, '')
    return s