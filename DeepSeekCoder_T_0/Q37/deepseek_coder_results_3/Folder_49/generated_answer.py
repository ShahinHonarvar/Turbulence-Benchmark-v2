def filter_chars(s):
    for i in range(42, 98):
        if '*' <= s[i] <= 'b':
            s = s.replace(s[i], '')
    return s