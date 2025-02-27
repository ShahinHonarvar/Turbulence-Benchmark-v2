def filter_chars(s):
    for i in range(34, 36):
        if '>' < s[i] < 'A':
            s = s.replace(s[i], '')
    return s