def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 32 < i < 84 and 'm' < c < 'w':
            continue
        t += c
    return t