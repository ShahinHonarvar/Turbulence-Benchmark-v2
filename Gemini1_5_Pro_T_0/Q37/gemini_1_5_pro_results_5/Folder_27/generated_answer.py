def filter_chars(s):
    for i in range(43, 81):
        if i < len(s) and '=' <= s[i] <= 'E':
            c = s[i]
            s = s.replace(c, '')
    return s