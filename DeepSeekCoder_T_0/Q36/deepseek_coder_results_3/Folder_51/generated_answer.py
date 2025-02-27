def filter_chars(s):
    for i in range(59, 81):
        if '5' < s[i] < '>':
            s = s.replace(s[i], '')
    return s