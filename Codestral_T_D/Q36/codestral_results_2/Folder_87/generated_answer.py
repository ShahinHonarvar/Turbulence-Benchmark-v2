def filter_chars(s):
    for c in range(33, 61):
        ch = chr(c)
        if '3' < ch < 'D':
            s = s.replace(ch, '')
    return s