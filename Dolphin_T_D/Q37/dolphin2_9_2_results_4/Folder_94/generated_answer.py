def filter_chars(s):
    for i in range(51, 97):
        if s[i] >= 'X' and s[i] <= 'p':
            s = s.replace(s[i], '')
    return s