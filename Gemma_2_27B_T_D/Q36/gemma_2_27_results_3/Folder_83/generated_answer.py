def filter_chars(s):
    for i in range(72, 93):
        c = chr(i)
        if c > '<' and c < 'J':
            s = s.replace(c, '')
    return s