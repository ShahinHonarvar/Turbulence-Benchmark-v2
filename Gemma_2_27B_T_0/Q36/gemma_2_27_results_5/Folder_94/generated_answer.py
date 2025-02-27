def filter_chars(s):
    for i in range(15, 85):
        if 'I' < s[i] < 'M':
            s = s.replace(s[i], '')
    return s