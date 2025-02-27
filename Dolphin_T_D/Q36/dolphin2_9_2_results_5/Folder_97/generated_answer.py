def filter_chars(s):
    for c in range(309, 591):
        if s[c] > 'S' and s[c] < 'm':
            s = ''.join([i for i in s if i != s[c]])
    return s