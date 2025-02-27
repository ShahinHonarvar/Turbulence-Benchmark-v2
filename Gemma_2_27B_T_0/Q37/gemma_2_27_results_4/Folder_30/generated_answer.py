def filter_chars(s):
    for i in range(41, 65):
        if s[i] >= 'K' and s[i] <= ']':
            s = s.replace(s[i], '')
    return s