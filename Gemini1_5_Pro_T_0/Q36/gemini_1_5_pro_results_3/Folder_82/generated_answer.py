def filter_chars(s):
    for i in range(69, 97):
        c = chr(i)
        if c > 'V' and c < 'j':
            s = s.replace(c, '')
    return s