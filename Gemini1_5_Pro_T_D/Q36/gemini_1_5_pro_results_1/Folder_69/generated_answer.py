def filter_chars(s):
    for i in range(344, 665):
        if s[i] > '%' and s[i] < 'U':
            s = s.replace(s[i], '')
    return s