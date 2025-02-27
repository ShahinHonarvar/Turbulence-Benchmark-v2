def filter_chars(s):
    for i in range(47, 74):
        if '&' < s[i] < 'M':
            s = s.replace(s[i], '')
    return s