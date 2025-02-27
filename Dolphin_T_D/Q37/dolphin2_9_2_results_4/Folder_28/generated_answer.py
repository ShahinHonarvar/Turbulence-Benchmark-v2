def filter_chars(s):
    s = list(s)
    for i in range(20, 80):
        if s[i] >= '!' and s[i] <= 'T':
            while s.count(s[i]) > 0:
                s.remove(s[i])
    return ''.join(s)