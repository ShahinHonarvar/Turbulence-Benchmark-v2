def filter_chars(s):
    for i in range(2):
        if i < len(s) and '*' <= s[i] <= 's':
            s = s.replace(s[i], '')
    return s