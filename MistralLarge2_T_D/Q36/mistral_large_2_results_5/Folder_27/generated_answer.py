def filter_chars(s):
    for i in range(48, 75):
        if i < len(s) and '6' < s[i] < '_':
            s = s.replace(s[i], '')
    return s