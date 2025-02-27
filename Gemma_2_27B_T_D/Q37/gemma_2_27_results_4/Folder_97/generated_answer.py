def filter_chars(s):
    for i in range(227, 236):
        if i < len(s) and 'D' <= s[i] <= 'u':
            s = s.replace(s[i], '')
    return s