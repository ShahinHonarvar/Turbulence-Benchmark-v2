def filter_chars(s):
    for c in s[21:44]:
        if '+' <= c <= '8':
            s = s.replace(c, '')
    return s