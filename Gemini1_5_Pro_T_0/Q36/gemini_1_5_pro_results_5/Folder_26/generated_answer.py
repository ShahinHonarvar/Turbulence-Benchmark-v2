def filter_chars(s):
    for i in range(43, 83):
        if i >= len(s):
            break
        if s[i] > ':' and s[i] < 'Q':
            c = s[i]
            s = s.replace(c, '')
    return s