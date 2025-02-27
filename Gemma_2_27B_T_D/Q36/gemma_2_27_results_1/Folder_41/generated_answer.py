def filter_chars(s):
    for i in range(81, 89):
        c = s[i]
        if c > 'f' and c < '{':
            s = s.replace(c, '')
    return s