def filter_chars(s):
    for i in range(79, 81):
        if 'S' < s[i] < '[':
            s = s.replace(s[i], '')
    return s