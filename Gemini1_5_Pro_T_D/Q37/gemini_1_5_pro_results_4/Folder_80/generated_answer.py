def filter_chars(s):
    for i in range(36, 80):
        if i < len(s) and 'a' <= s[i] <= 'i':
            s = s.replace(s[i], '')
    return s