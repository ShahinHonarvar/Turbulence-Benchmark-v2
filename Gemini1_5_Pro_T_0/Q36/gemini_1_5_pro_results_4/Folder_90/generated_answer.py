def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 344 <= i <= 874 and 'f' < c < '~':
            continue
        t += c
    return t