def filter_chars(s):
    for i in range(18, 82):
        if s[i] >= 'W' and s[i] <= '[':
            s = s.replace(s[i], '')
    return s