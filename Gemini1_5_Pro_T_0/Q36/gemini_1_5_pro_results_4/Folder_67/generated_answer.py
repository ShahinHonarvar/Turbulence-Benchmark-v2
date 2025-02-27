def filter_chars(s):
    for i in range(18, 31):
        if i >= len(s):
            break
        c = s[i]
        if 'H' < c < '|':
            s = s.replace(c, '')
    return s