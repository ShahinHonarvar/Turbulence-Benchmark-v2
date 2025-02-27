def filter_chars(s):
    s = list(s)
    for i in range(32, 47):
        if '0' <= s[i] <= 'k':
            while s[i] in s:
                s.remove(s[i])
    return ''.join(s)