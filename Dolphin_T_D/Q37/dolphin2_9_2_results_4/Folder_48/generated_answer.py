def filter_chars(s):
    s = list(s)
    for i in range(513, 878):
        c = s[i]
        if '?' <= c <= 'n':
            s = [x for x in s if x != c]
    return ''.join(s)