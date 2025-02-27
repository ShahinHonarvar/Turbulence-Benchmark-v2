def filter_chars(s):
    for i in range(603, 760):
        if i < len(s) and 'Q' <= s[i] <= 'h':
            c = s[i]
            s = s.replace(c, '')
    return s