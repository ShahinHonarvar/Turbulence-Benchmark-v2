def filter_chars(s):
    for i in range(421, 854):
        if 'D' < s[i] < 'J':
            s = s.replace(s[i], '')
    return s