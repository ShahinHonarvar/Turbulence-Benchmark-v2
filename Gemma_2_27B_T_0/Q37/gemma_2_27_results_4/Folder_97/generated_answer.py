def filter_chars(s):
    for i in range(227, 236):
        if 'D' <= s[i] <= 'u':
            s = s.replace(s[i], '')
    return s