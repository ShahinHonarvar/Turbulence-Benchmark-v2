def filter_chars(s):
    for i in range(86, 93):
        if 'E' < s[i] < '~':
            c = s[i]
            s = ''.join([x for x in s if x != c])
    return s