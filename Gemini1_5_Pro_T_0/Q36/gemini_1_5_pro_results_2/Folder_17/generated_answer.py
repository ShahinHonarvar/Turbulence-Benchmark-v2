def filter_chars(s):
    for i in range(18, 95):
        if i < len(s) and s[i] > 'K' and (s[i] < 'a'):
            c = s[i]
            s = s.replace(c, '')
    return s