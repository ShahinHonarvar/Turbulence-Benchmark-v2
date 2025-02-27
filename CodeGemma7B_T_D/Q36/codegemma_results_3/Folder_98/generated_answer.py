def filter_chars(s):
    for i in range(4, 8):
        for j in range(s.count(s[i])):
            s = s[:s.index(s[i])] + s[s.index(s[i]) + 1:]
    return s