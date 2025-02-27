def filter_chars(s):
    for i in range(42, 68):
        if len(s) > i and 't' < s[i] < 'x':
            s = s.replace(s[i], '')
    return s