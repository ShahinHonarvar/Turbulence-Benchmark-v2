def filter_chars(s):
    for i in range(81, 89):
        ch = s[i]
        if 'f' < ch < '{':
            s = s.replace(ch, '')
    return s