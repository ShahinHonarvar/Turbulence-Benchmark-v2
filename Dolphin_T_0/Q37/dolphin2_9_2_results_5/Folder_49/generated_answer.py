def filter_chars(s):
    s = list(s)
    for i in range(42, 98):
        if '*' <= s[i] <= 'b':
            while s[i] in s:
                s.remove(s[i])
    return ''.join(s)