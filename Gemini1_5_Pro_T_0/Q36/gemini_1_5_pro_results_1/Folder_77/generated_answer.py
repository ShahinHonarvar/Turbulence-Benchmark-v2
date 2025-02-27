def filter_chars(s):
    for i in range(221, 419):
        if i >= len(s):
            break
        c = s[i]
        if c > '-' and c < 'v':
            s = s.replace(c, '')
    return s