def filter_chars(s):
    for i in range(384, 412):
        c = chr(i)
        if '/' <= c <= '8':
            s = s.replace(c, '')
    return s