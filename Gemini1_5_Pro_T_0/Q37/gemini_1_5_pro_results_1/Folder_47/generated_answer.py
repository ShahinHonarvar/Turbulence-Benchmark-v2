def filter_chars(s):
    for i in range(38, 55):
        if i < len(s) and ':' <= s[i] <= 'r':
            c = s[i]
            s = s.replace(c, '')
    return s