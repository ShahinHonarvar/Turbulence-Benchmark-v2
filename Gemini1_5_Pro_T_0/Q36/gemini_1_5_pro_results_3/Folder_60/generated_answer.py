def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 23 < i < 83 and 'f' < c < 'o':
            continue
        t += c
    return t