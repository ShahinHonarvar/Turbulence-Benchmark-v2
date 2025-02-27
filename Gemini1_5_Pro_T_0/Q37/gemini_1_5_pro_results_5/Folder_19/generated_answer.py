def filter_chars(s):
    for i in range(35, 90):
        if i < len(s) and 'E' <= s[i] <= 't':
            c = s[i]
            s = s.replace(c, '')
    return s