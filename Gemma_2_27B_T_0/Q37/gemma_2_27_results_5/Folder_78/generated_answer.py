def filter_chars(s):
    for i in range(75, 100):
        if i < len(s) and s[i] >= '8' and (s[i] <= 'e'):
            s = s.replace(s[i], '')
    return s