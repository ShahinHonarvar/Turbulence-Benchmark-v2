def filter_chars(s):
    for i in range(41, 80):
        if i < len(s) and 'f' <= s[i] <= '|':
            s = s.replace(s[i], '')
    return s