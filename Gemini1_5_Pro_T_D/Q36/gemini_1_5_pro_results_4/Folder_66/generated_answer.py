def filter_chars(s):
    for i in range(39, 87):
        if s[i] > '!' and s[i] < '}':
            c = s[i]
            s = s.replace(c, '')
    return s