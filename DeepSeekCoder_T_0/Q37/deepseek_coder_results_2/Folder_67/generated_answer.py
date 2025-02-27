def filter_chars(s):
    for i in range(19, 23):
        if len(s) > i and ']' <= s[i] <= 't':
            s = s.replace(s[i], '')
    return s