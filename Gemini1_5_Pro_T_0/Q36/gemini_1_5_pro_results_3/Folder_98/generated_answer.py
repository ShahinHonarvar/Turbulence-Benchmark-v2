def filter_chars(s):
    for i in range(4, 8):
        if i >= len(s):
            break
        c = s[i]
        if '1' < c < 'J':
            s = s.replace(c, '')
    return s