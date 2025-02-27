def filter_chars(s):
    for i in range(24, 45):
        if '3' < s[i] < 'I':
            s = s.replace(s[i], '')
    return s