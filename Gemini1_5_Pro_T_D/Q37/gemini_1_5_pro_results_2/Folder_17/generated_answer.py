def filter_chars(s):
    for i in range(27, 30):
        if i < len(s) and ';' <= s[i] <= 'b':
            c = s[i]
            s = s.replace(c, '')
    return s