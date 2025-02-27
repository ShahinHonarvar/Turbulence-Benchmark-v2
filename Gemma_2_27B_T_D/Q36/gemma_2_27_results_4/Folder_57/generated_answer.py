def filter_chars(s):
    for i in range(70, 74):
        if i < len(s) and s[i] > 'A' and (s[i] < 'U'):
            s = s.replace(s[i], '')
    return s