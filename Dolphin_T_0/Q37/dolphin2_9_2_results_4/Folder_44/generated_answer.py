def filter_chars(s):
    for i in range(21, 44):
        if s[i] >= '+' and s[i] <= '8':
            return s.replace(s[i], '')
    return s