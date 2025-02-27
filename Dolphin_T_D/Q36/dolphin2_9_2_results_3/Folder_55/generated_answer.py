def filter_chars(s):
    for i in range(3, 5):
        if s[i] > 'Y' and s[i] < 's':
            s = s.replace(s[i], '')
    return s