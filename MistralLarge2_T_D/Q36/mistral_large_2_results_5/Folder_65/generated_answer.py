def filter_chars(s):
    for i in range(58, 82):
        if 'F' < s[i] < 'O':
            s = s.replace(s[i], '')
    return s