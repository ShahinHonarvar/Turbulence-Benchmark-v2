def filter_chars(s):
    for i in range(83, 100):
        if i < len(s):
            if s[i] >= '*' and s[i] <= 'j':
                s = s.replace(s[i], '')
    return s