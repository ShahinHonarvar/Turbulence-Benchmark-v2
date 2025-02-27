def filter_chars(s):
    for i in range(154, 222):
        if i < len(s) and 'A' < s[i] < 'f':
            c = s[i]
            s = s.replace(c, '')
    return s