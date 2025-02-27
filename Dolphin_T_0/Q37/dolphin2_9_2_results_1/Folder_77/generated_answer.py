def filter_chars(s):
    for i in range(384, 412):
        if s[i] >= '/' and s[i] <= '8':
            s = s.replace(s[i], '')
    return s