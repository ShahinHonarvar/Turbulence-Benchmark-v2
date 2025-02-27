def filter_chars(s):
    for i in range(63, 85):
        if i < len(s):
            c = s[i]
            if 'E' <= c <= '~':
                s = s.replace(c, '')
    return s