def filter_chars(s):
    for i in range(384, 412):
        if i < len(s) and s[i] >= '/' and (s[i] <= '8'):
            c = s[i]
            s = s.replace(c, '')
    return s