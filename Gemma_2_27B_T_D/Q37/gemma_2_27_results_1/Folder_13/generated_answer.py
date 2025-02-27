def filter_chars(s):
    for i in range(124, 855):
        if i < len(s) and s[i] >= '9' and (s[i] <= 's'):
            s = s.replace(s[i], '')
    return s