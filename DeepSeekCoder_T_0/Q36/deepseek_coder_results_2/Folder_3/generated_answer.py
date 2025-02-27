def filter_chars(s):
    for i in range(43, 78):
        if '!' < s[i] < '?':
            s = s.replace(s[i], '')
    return s