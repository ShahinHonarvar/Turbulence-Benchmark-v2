def filter_chars(s):
    s = list(s)
    for i in range(19, 33):
        if 'f' <= s[i] <= 'o':
            while s[i] in s:
                s.remove(s[i])
    return ''.join(s)