def filter_chars(s):
    for i in range(22, 25):
        if s[i] > '5' and s[i] < '}':
            s = s.replace(s[i], '')
    return s