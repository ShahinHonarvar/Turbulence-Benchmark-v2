def filter_chars(s):
    for i in range(23, 45):
        while s[i] > '3' and s[i] < 'I' and (s.count(s[i]) > 1):
            while s.count(s[i]) > 1:
                s = s.replace(s[i], '', 1)
    return s