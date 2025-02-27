def filter_chars(s):
    s = list(s)
    for i in range(515, 539):
        if '+' <= s[i] <= '}':
            while s[i] in s:
                s.remove(s[i])
    return ''.join(s)