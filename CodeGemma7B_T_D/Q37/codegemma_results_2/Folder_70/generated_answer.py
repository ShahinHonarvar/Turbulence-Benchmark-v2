def filter_chars(s):
    for i in range(515, 539):
        for j in range(s.count(s[i])):
            s = s[:j] + s[j + 1:]
    return s