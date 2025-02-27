def filter_chars(s):
    for i in range(51, 92):
        if s[i] > 'A' and s[i] < 'Q':
            s = s.replace(s[i], '')
    return s