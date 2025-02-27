def filter_chars(s):
    for i in range(1, 6):
        if '$' <= s[i] <= ';':
            s = s.replace(s[i], '')
    return s