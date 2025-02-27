def filter_chars(s):
    for i in range(13, 40):
        if i < len(s) and ':' < s[i] < 'C':
            s = s.replace(s[i], '')
    return s