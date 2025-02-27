def filter_chars(s):
    for i in range(43, 68):
        if i < len(s) and 't' < s[i] < 'x':
            s = s.replace(s[i], '')
    return s