def filter_chars(s):
    for i in range(81, 89):
        if 'f' < s[i] < '{':
            s = s.replace(s[i], '')
    return s