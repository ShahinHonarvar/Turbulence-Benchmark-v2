def filter_chars(s):
    for i in range(373, 902):
        if i < len(s) and 'T' <= s[i] <= 'h':
            c = s[i]
            s = s.replace(c, '')
    return s