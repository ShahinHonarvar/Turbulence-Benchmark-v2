def filter_chars(s):
    for i in range(2, 6):
        if ',' < s[i] < 'f':
            s = s.replace(s[i], '')
    return s