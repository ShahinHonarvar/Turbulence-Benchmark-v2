def filter_chars(s):
    for i in range(20, 80):
        if '!' <= s[i] <= 'T':
            s = s.replace(s[i], '')
    return s