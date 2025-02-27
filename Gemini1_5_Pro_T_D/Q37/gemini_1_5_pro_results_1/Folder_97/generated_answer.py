def filter_chars(s):
    for i in range(227, 236):
        if i < len(s) and 'D' <= s[i] <= 'u':
            c = s[i]
            s = s.replace(c, '')
    return s