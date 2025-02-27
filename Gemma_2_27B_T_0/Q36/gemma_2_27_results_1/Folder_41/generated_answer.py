def filter_chars(s):
    for i in range(81, 89):
        if s[i] > 'f' and s[i] < '{':
            s = s.replace(s[i], '')
    return s