def filter_chars(s):
    for i in range(521, 723):
        if i < len(s) and s[i] >= '>' and (s[i] <= '_'):
            s = s.replace(s[i], '')
    return s