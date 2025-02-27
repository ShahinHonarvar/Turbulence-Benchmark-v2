def filter_chars(s):
    for i in range(41, 80):
        if len(s) > i and 'f' <= s[i] <= '|':
            s = s.replace(s[i], '')
    return s