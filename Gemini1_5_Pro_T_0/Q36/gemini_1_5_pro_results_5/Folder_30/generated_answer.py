def filter_chars(s):
    for i in range(23, 45):
        if i < len(s) and '3' < s[i] < 'I':
            s = s.replace(s[i], '')
    return s