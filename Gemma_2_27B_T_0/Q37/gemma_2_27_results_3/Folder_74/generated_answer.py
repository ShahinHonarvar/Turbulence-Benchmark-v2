def filter_chars(s):
    for i in range(19, 33):
        if i < len(s) and s[i] >= 'f' and (s[i] <= 'o'):
            s = s.replace(s[i], '')
    return s