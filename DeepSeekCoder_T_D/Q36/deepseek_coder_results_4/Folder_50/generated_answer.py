def filter_chars(s):
    for i in range(62, 88):
        if '%' < s[i] < 'q':
            s = s.replace(s[i], '')
    return s