def filter_chars(s):
    for i in range(477, 985):
        c = s[i]
        if ',' <= c <= 'V':
            s = s.replace(c, '')
    return s