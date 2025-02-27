def filter_chars(s):
    for i in range(52, 88):
        ch = s[i]
        if '&' < ch < 'c':
            s = s.replace(ch, '')
    return s