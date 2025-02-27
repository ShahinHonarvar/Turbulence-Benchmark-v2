def filter_chars(s):
    for i in range(22, 86):
        if '7' <= s[i] <= 'e':
            s = s.replace(s[i], '')
    return s