def filter_chars(s):
    for i in range(24, 83):
        if len(s) > i and s[i] >= '5' and (s[i] <= '<'):
            s = s.replace(s[i], '')
    return s