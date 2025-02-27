def filter_chars(s):
    for i in range(5, 8):
        if s[i] > '1' and s[i] < 'J':
            s = s.replace(s[i], '')
    return s