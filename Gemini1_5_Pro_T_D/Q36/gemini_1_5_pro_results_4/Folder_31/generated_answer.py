def filter_chars(s):
    for i in range(14, 75):
        if i >= len(s):
            break
        if s[i] > '9' and s[i] < 'K':
            s = s.replace(s[i], '')
    return s