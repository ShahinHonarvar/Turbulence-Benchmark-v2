def filter_chars(s):
    for i in range(4, 8):
        for c in s:
            if c > '1' and c < 'J':
                s = s.replace(c, '')
    return s