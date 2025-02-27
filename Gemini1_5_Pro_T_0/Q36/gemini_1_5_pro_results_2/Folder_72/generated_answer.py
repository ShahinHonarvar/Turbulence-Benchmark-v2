def filter_chars(s):
    for i in range(44, 68):
        if i >= len(s):
            break
        if s[i] > 'W' and s[i] < 'x':
            s = s.replace(s[i], '')
    return s