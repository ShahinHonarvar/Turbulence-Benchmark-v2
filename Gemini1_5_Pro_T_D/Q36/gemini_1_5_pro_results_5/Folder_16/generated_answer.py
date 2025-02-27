def filter_chars(s):
    t = list(s)
    for i in range(332, 713):
        if i < len(s) and 'M' < s[i] < '_':
            c = s[i]
            t = list(filter(lambda x: x != c, t))
    return ''.join(t)