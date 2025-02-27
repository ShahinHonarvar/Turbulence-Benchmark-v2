def filter_chars(s):
    for i in range(63, 85):
        if i < len(s) and 'E' <= s[i] <= '~':
            c = s[i]
            s = s.replace(c, '')
    return s