def filter_chars(s):
    for i in range(78, 81):
        if s[i] > 'S' and s[i] < '[':
            s = s.replace(s[i], '', 1)
    return s