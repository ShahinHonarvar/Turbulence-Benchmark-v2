def filter_chars(s):
    for i in range(770, 971):
        if i >= len(s):
            break
        c = s[i]
        if '-' <= c <= 'D':
            s = s.replace(c, '')
    return s