def filter_chars(s):
    for i in range(81, 89):
        if i < len(s) and 'f' < s[i] < '{':
            c = s[i]
            s = s.replace(c, '')
    return s