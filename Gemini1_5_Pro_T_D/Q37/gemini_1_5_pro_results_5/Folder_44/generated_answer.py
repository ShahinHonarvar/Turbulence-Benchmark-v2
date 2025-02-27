def filter_chars(s):
    for i in range(21, 44):
        if i < len(s) and '+' <= s[i] <= '8':
            c = s[i]
            s = s.replace(c, '')
    return s