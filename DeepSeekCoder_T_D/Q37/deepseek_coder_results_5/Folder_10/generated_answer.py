def filter_chars(s):
    for i in range(63, 85):
        if 'E' <= s[i] <= '~':
            s = s.replace(s[i], '')
    return s