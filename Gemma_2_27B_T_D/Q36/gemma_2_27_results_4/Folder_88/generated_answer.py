def filter_chars(s):
    for i in range(78, 81):
        if len(s) > i and 'S' < s[i] < '[':
            s = s.replace(s[i], '')
    return s