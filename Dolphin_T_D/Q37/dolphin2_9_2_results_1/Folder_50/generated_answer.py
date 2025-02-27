def filter_chars(s):
    for i in range(71, 97):
        if s[i] >= '_' and s[i] <= 'o':
            s = s.replace(s[i], '')
    return s