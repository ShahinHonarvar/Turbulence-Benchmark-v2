def filter_chars(s):
    for i in range(57, 97):
        if s[i] >= '<' and s[i] <= 'w':
            s = s.replace(s[i], '')
    return s