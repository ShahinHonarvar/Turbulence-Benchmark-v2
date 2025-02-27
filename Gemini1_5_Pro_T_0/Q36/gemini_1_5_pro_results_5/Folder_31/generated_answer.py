def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 14 < i < 75 and '9' < c < 'K':
            continue
        t += c
    return t