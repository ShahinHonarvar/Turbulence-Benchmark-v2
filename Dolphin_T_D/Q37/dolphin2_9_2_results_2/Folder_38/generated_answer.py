def filter_chars(s):
    s = list(s)
    for i in range(24, 80):
        if 'a' <= s[i] <= 'f':
            while s[i] in s:
                s.remove(s[i])
    return ''.join(s)