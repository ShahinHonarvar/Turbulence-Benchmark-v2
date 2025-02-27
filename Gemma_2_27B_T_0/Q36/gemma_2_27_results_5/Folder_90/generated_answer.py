def filter_chars(s):
    for i in range(344, 874):
        if s[i] > 'f' and s[i] < '~':
            s = s.replace(s[i], '')
    return s