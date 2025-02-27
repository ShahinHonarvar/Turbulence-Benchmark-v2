def filter_chars(s):
    for i in range(19, 91):
        if i < len(s) and 'F' <= s[i] <= 'h':
            s = s.replace(s[i], '')
    return s