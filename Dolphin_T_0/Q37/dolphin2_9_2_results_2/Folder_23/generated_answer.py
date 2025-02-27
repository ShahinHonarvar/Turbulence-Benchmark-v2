def filter_chars(s):
    for i in range(51, 78):
        if s[i] >= 'V' and s[i] <= 'Y':
            s = s.replace(s[i], '')
    return s