def filter_chars(s):
    for i in range(587, 648):
        if i >= len(s):
            break
        if s[i] > ',' and s[i] < 'c':
            s = s.replace(s[i], '')
    return s