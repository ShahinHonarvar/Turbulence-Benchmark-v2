def filter_chars(s):
    for i in range(41, 65):
        if 'K' <= s[i] <= ']':
            s = s.replace(s[i], '')
    return s