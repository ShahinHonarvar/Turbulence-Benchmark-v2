def filter_chars(s):
    for i in range(43, 69):
        while s[i] > 'B' and s[i] < 'r':
            s[i] = ''
    return s