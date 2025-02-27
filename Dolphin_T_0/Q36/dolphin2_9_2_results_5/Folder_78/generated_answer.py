def filter_chars(s):
    for i in range(29, 34):
        if s[i] > '%' and s[i] < 'a':
            s = s.replace(s[i], '')
    return s