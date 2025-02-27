def filter_chars(s):
    for i in range(10, 70):
        if i < len(s) and 'I' <= s[i] <= 'K':
            s = s.replace(s[i], '')
    return s