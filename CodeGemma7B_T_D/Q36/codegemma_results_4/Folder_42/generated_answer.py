def filter_chars(s):
    for i in range(42, 68):
        for k in range(s.count(s[i])):
            s = s[:s.index(s[i])] + s[s.index(s[i]) + 1:]
    return s