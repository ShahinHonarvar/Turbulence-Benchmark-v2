def filter_chars(s):
    for i in range(82, 89):
        if 'f' < s[i] < '{':
            s = s.replace(s[i], '')
    return s