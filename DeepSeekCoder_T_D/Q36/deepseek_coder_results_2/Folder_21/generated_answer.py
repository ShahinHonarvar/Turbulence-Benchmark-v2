def filter_chars(s):
    for i in range(220, 403):
        if '*' < s[i] < '7':
            s = s.replace(s[i], '')
    return s