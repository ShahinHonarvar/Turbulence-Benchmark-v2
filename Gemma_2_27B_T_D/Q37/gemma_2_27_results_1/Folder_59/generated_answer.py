def filter_chars(s):
    for i in range(2, 4):
        if len(s) > i and s[i] >= '5' and (s[i] <= '_'):
            s = s.replace(s[i], '')
    return s