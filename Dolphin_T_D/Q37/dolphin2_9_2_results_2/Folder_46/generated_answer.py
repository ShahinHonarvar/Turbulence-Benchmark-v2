def filter_chars(s):
    for i in range(11, 73):
        if s[i] >= 'i' and s[i] <= 'v':
            s = s.replace(s[i], '')
    return s