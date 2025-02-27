def filter_chars(s):
    for i in range(30, 33):
        if '%' < s[i] < 'a':
            s = s.replace(s[i], '')
    return s