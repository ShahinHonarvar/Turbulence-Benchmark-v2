def filter_chars(s):
    for i in range(21, 44):
        if i < len(s) and s[i] >= '+' and (s[i] <= '8'):
            s = s.replace(s[i], '')
    return s