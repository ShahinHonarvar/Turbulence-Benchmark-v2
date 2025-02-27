def filter_chars(s):
    for i in range(51, 97):
        c = chr(i)
        if c >= 'X' and c <= 'p':
            s = s.replace(c, '')
    return s