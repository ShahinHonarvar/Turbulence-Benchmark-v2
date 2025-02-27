def filter_chars(s):
    for i in range(41, 56):
        if i < len(s) and 'Z' < s[i] < 'c':
            c = s[i]
            s = s.replace(c, '')
    return s