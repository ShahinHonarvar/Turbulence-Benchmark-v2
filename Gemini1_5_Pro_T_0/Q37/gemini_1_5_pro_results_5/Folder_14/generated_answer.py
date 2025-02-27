def filter_chars(s):
    for i in range(35, 99):
        if i < len(s) and 'A' <= s[i] <= 'b':
            c = s[i]
            s = s.replace(c, '')
    return s