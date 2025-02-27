def filter_chars(s):
    for i in range(14, 40):
        if i < len(s) and s[i] > ':' and (s[i] < 'C'):
            s = s.replace(s[i], '')
    return s