def filter_chars(s):
    for i in range(79, 81):
        if i < len(s) and 'S' < s[i] < '[':
            s = s.replace(s[i], '')
    return s