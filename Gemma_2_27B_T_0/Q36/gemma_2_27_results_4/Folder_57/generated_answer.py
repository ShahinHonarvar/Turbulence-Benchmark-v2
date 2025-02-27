def filter_chars(s):
    for i in range(70, 74):
        if i < len(s) and 'A' < s[i] < 'U':
            s = s.replace(s[i], '')
    return s