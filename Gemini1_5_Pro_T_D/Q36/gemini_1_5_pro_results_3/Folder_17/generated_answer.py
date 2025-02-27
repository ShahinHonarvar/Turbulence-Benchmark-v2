def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 18 < i < 95 and 'K' < c < 'a':
            continue
        t += c
    return t