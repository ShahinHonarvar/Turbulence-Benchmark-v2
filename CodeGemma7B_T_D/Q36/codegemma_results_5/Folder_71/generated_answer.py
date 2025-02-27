def filter_chars(s):
    for i in range(82, 89):
        if s[i] > '*' and s[i] < '[':
            while s.find(s[i]) != -1:
                s = s[:s.find(s[i])] + s[s.find(s[i]) + 1:]
    return s