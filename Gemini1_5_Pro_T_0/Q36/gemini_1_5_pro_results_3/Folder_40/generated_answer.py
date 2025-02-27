def filter_chars(s):
    for i in range(2, 6):
        if s[i] > '-' and s[i] < 'L':
            s = s.replace(s[i], '')
    return s