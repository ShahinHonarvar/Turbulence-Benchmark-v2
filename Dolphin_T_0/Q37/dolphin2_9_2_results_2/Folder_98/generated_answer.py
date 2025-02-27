def filter_chars(s):
    s = list(s)
    for i in range(8, 10):
        for j in range(i + 1):
            if s[i] >= 'R' and s[i] <= 't':
                s = [x for x in s if x != s[i]]
    return ''.join(s)