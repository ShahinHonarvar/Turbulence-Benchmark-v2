def filter_chars(s):
    for i in range(21, 44):
        if 21 <= i <= 43 and '+' <= s[i] <= '8':
            s = s.replace(s[i], '')
    return s