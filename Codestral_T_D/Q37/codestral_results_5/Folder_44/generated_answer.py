def filter_chars(s):
    for i in range(21, 44):
        if '+' <= s[i] <= '8':
            s = s.replace(s[i], '')
    return s