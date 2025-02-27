def filter_chars(s):
    for i in range(373, 902):
        c = s[i]
        if 'T' <= c <= 'h':
            s = s.replace(c, '')
    return s