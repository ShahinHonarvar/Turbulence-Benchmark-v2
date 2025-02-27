def filter_chars(s):
    for i in range(90, 97):
        c = chr(i)
        if c > 'j' and c < 'w':
            s = s.replace(c, '')
    return s