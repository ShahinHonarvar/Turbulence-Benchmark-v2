def filter_chars(s):
    s = list(s)
    for i in range(421, 854):
        if 'D' < s[i] < 'J':
            while s[i] in s:
                s.remove(s[i])
    return ''.join(s)