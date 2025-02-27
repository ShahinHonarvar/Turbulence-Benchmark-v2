def filter_chars(s):
    for i in range(3, 8):
        if i >= len(s):
            break
        if s[i] > '?' and s[i] < 'k':
            s = s.replace(s[i], '')
    return s